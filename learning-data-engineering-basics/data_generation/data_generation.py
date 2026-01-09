"""Realistic OLTP-style payroll data generation for PostgreSQL.

This script:
- Creates master tables for departments, designations, and salary structures
- Maps designations to salary structures (fixed percentage breakdowns)
- Creates employee records with join/exit dates
- Generates daily attendance only for active employees on working days
- Generates monthly payroll based on base salary and salary structure
- Applies simple rule-based deductions (PF, tax, professional tax)
- Inserts rows in batches with periodic commits
- Performs basic validation checks at the end

Configure the PostgreSQL connection via environment variables or edit DEFAULT_DB_CONFIG.
"""

import os
import random
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

import psycopg2
from psycopg2.extras import execute_batch
from faker import Faker
from tqdm import tqdm


DEFAULT_DB_CONFIG = {
    "host": os.getenv("PGHOST", "localhost"),
    "port": int(os.getenv("PGPORT", "5432")),
    "dbname": os.getenv("PGDATABASE", "oltp_olap"),
    "user": os.getenv("PGUSER", "rohitagarwal"),
    "password": os.getenv("PGPASSWORD", "rohit2610"),
}

faker = Faker("en_IN")


@dataclass
class SalaryStructure:
    code: str
    hra_pct: float
    da_pct: float
    allowance_pct: float


def get_connection():
    return psycopg2.connect(**DEFAULT_DB_CONFIG)


def create_schema(conn) -> None:
    """Create tables if they do not exist.

    The design enforces salary structure immutability per designation via FK.
    """

    ddl = """
	CREATE TABLE IF NOT EXISTS department (
		department_id SERIAL PRIMARY KEY,
		name          TEXT NOT NULL UNIQUE
	);

	CREATE TABLE IF NOT EXISTS salary_structure (
		structure_id   SERIAL PRIMARY KEY,
		code           TEXT NOT NULL UNIQUE,
		hra_pct        NUMERIC(5,2) NOT NULL,
		da_pct         NUMERIC(5,2) NOT NULL,
		allowance_pct  NUMERIC(5,2) NOT NULL,
		CHECK (hra_pct >= 0 AND da_pct >= 0 AND allowance_pct >= 0),
		CHECK (hra_pct + da_pct + allowance_pct <= 100.0)
	);

	CREATE TABLE IF NOT EXISTS designation (
		designation_id SERIAL PRIMARY KEY,
		title          TEXT NOT NULL UNIQUE,
		structure_id   INT NOT NULL REFERENCES salary_structure(structure_id)
	);

	CREATE TABLE IF NOT EXISTS employee (
		employee_id    SERIAL PRIMARY KEY,
		full_name      TEXT NOT NULL,
		department_id  INT NOT NULL REFERENCES department(department_id),
		designation_id INT NOT NULL REFERENCES designation(designation_id),
		base_salary    NUMERIC(12,2) NOT NULL,
		join_date      DATE NOT NULL,
		exit_date      DATE NULL,
		CHECK (exit_date IS NULL OR exit_date >= join_date)
	);

	CREATE TABLE IF NOT EXISTS attendance (
		attendance_id SERIAL PRIMARY KEY,
		employee_id   INT NOT NULL REFERENCES employee(employee_id),
		att_date      DATE NOT NULL,
		status        TEXT NOT NULL CHECK (status IN ('P', 'A', 'L')),
		UNIQUE (employee_id, att_date)
	);

	CREATE TABLE IF NOT EXISTS payroll_monthly (
		payroll_id     SERIAL PRIMARY KEY,
		employee_id    INT NOT NULL REFERENCES employee(employee_id),
		year_month     DATE NOT NULL,
		base_salary    NUMERIC(12,2) NOT NULL,
		hra_amount     NUMERIC(12,2) NOT NULL,
		da_amount      NUMERIC(12,2) NOT NULL,
		allowance_amt  NUMERIC(12,2) NOT NULL,
		gross_salary   NUMERIC(12,2) NOT NULL,
		pf_deduction   NUMERIC(12,2) NOT NULL,
		tax_deduction  NUMERIC(12,2) NOT NULL,
		prof_tax       NUMERIC(12,2) NOT NULL,
		net_salary     NUMERIC(12,2) NOT NULL,
		UNIQUE (employee_id, year_month)
	);
	"""

    with conn.cursor() as cur:
        cur.execute(ddl)
    conn.commit()


def seed_master_data(conn) -> None:
    """Insert deterministic master data if not present."""
    # Generate ~150 realistic department names
    num_departments = 150
    departments = [
        f"Dept {i + 1:03d} - {faker.company()}" for i in range(num_departments)
    ]

    structures = [
        SalaryStructure("JUNIOR", 20.0, 30.0, 10.0),
        SalaryStructure("MID", 25.0, 35.0, 15.0),
        SalaryStructure("SENIOR", 30.0, 40.0, 20.0),
        # Ensure total percentage <= 100 to satisfy CHECK constraint
        SalaryStructure("LEAD", 35.0, 40.0, 20.0),
    ]

    designations = [
        ("Junior Engineer", "JUNIOR"),
        ("Engineer", "MID"),
        ("Senior Engineer", "SENIOR"),
        ("Lead Engineer", "LEAD"),
        ("HR Executive", "MID"),
        ("HR Manager", "SENIOR"),
        ("Accountant", "MID"),
        ("Finance Manager", "SENIOR"),
        ("Sales Executive", "JUNIOR"),
        ("Sales Manager", "SENIOR"),
        ("Operations Executive", "JUNIOR"),
        ("Operations Manager", "SENIOR"),
    ]

    with conn.cursor() as cur:
        # Departments
        cur.executemany(
            "INSERT INTO department(name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
            [(d,) for d in departments],
        )

        # Salary structures
        cur.executemany(
            """
			INSERT INTO salary_structure(code, hra_pct, da_pct, allowance_pct)
			VALUES (%s, %s, %s, %s)
			ON CONFLICT (code) DO NOTHING
			""",
            [(s.code, s.hra_pct, s.da_pct, s.allowance_pct) for s in structures],
        )

        # Fetch structure ids
        cur.execute("SELECT structure_id, code FROM salary_structure")
        structure_map: Dict[str, int] = {code: sid for sid, code in cur.fetchall()}

        # Designations mapped to structures (policy: fixed mapping)
        cur.executemany(
            """
			INSERT INTO designation(title, structure_id)
			VALUES (%s, %s)
			ON CONFLICT (title) DO NOTHING
			""",
            [
                (title, structure_map[struct_code])
                for title, struct_code in designations
                if struct_code in structure_map
            ],
        )

    conn.commit()


def random_name() -> str:
    # Use Faker for more realistic Indian-style names
    return faker.name()


def daterange(start: date, end: date):
    for n in range((end - start).days + 1):
        yield start + timedelta(days=n)


def generate_employees(
    conn,
    num_employees: int = 10_000,
    start_join_date: date = date(2018, 1, 1),
    end_join_date: date = date(2024, 12, 31),
    exit_probability: float = 0.3,
) -> None:
    """Generate employees with random departments/designations/base salaries.

    Some employees get an exit_date after join_date; others remain active.
    """

    with conn.cursor() as cur:
        cur.execute("SELECT department_id FROM department")
        departments = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT designation_id FROM designation")
        designations = [row[0] for row in cur.fetchall()]

        if not departments or not designations:
            raise RuntimeError("Master data not seeded correctly")

        employees_batch = []
        for _ in tqdm(range(num_employees), desc="Generating employees"):
            dept_id = random.choice(departments)
            desig_id = random.choice(designations)

            # Base salary by designation seniority (rough heuristic)
            base_salary = random.randint(25000, 90000)

            join_dt_ordinal = random.randint(
                start_join_date.toordinal(), end_join_date.toordinal()
            )
            join_dt = date.fromordinal(join_dt_ordinal)

            if random.random() < exit_probability:
                # Exit between 6 months and 3 years after join
                min_exit = join_dt + timedelta(days=180)
                max_exit = join_dt + timedelta(days=365 * 3)
                if max_exit > end_join_date:
                    max_exit = end_join_date
                if min_exit >= max_exit:
                    exit_dt = None
                else:
                    exit_dt = min_exit + timedelta(
                        days=random.randint(0, (max_exit - min_exit).days)
                    )
            else:
                exit_dt = None

            employees_batch.append(
                (
                    random_name(),
                    dept_id,
                    desig_id,
                    float(base_salary),
                    join_dt,
                    exit_dt,
                )
            )

        execute_batch(
            cur,
            """
			INSERT INTO employee(
				full_name, department_id, designation_id,
				base_salary, join_date, exit_date
			)
			VALUES (%s, %s, %s, %s, %s, %s)
			""",
            employees_batch,
            page_size=1000,
        )

    conn.commit()


def generate_attendance(
    conn,
    start_date: date = date(2020, 1, 1),
    end_date: date = date(2024, 12, 31),
    batch_size: int = 5000,
) -> None:
    """Generate daily attendance for active employees on working days only.

    status: 'P' (present), 'A' (absent), 'L' (leave).
    Weekends are skipped.
    """

    with conn.cursor() as cur:
        cur.execute("SELECT employee_id, join_date, exit_date FROM employee")
        employees = cur.fetchall()

    def is_active(emp_join: date, emp_exit: Optional[date], day: date) -> bool:
        if day < emp_join:
            return False
        if emp_exit and day > emp_exit:
            return False
        return True

    total_days = (end_date - start_date).days + 1

    batch: List[Tuple[int, date, str]] = []
    with conn.cursor() as cur:
        for day in tqdm(
            daterange(start_date, end_date),
            total=total_days,
            desc="Generating attendance (per day)",
        ):
            # Skip weekends
            if day.weekday() >= 5:
                continue

            for emp_id, join_dt, exit_dt in employees:
                if not is_active(join_dt, exit_dt, day):
                    continue

                r = random.random()
                if r < 0.88:
                    status = "P"
                elif r < 0.96:
                    status = "A"
                else:
                    status = "L"

                batch.append((emp_id, day, status))

                if len(batch) >= batch_size:
                    execute_batch(
                        cur,
                        """
						INSERT INTO attendance(employee_id, att_date, status)
						VALUES (%s, %s, %s)
						ON CONFLICT (employee_id, att_date) DO NOTHING
						""",
                        batch,
                    )
                    conn.commit()
                    batch.clear()

        if batch:
            execute_batch(
                cur,
                """
				INSERT INTO attendance(employee_id, att_date, status)
				VALUES (%s, %s, %s)
				ON CONFLICT (employee_id, att_date) DO NOTHING
				""",
                batch,
            )
            conn.commit()


def compute_deductions(gross: float) -> Tuple[float, float, float]:
    """Simple deterministic deduction rules.

    - PF: 12% of base-ish (approx via gross * 0.12 * 0.4)
    - Tax: slab based on gross
    - Professional tax: flat 200 for gross >= 20k, else 0
    """

    pf = round(gross * 0.12 * 0.4, 2)

    if gross <= 25000:
        tax = round(gross * 0.05, 2)
    elif gross <= 60000:
        tax = round(gross * 0.10, 2)
    else:
        tax = round(gross * 0.20, 2)

    prof_tax = 200.0 if gross >= 20000 else 0.0
    return pf, tax, prof_tax


def generate_monthly_payroll(
    conn,
    start_year: int = 2020,
    end_year: int = 2024,
    batch_size: int = 2000,
) -> None:
    """Generate monthly payroll only for months with presence.

    - Uses salary structure percentages tied to designation
    - Considers only employees active in that month
    - Inserts payroll rows only when the employee has at least 1 present day
    - Covers all months from start_year through end_year (inclusive)
    """

    with conn.cursor() as cur:
        # Map designation -> salary structure percentages
        cur.execute(
            """
			SELECT d.designation_id,
				   s.hra_pct, s.da_pct, s.allowance_pct
			FROM designation d
			JOIN salary_structure s ON d.structure_id = s.structure_id
			"""
        )
        struct_by_designation: Dict[int, Tuple[float, float, float]] = {
            desig_id: (float(hra), float(da), float(allow))
            for desig_id, hra, da, allow in cur.fetchall()
        }

        # Load employees with designation and active range
        cur.execute(
            """
			SELECT employee_id, designation_id, base_salary, join_date, exit_date
			FROM employee
			"""
        )
        employees = cur.fetchall()

    def month_start_end(y: int, m: int) -> Tuple[date, date]:
        start = date(y, m, 1)
        if m == 12:
            end = date(y + 1, 1, 1) - timedelta(days=1)
        else:
            end = date(y, m + 1, 1) - timedelta(days=1)
        return start, end

    # Precompute all (year, month) pairs so tqdm can track total progress
    months = [(y, m) for y in range(start_year, end_year + 1) for m in range(1, 13)]

    batch: List[Tuple] = []
    with conn.cursor() as cur:
        for year, month in tqdm(months, desc="Generating monthly payroll"):
            m_start, m_end = month_start_end(year, month)

            # Preload attendance counts for the month for efficiency
            cur.execute(
                """
				SELECT employee_id,
					   SUM(CASE WHEN status = 'P' THEN 1 ELSE 0 END) AS present_days
				FROM attendance
				WHERE att_date BETWEEN %s AND %s
				GROUP BY employee_id
				""",
                (m_start, m_end),
            )
            attendance_present: Dict[int, int] = {
                emp_id: int(present) for emp_id, present in cur.fetchall()
            }

            for emp_id, desig_id, base_salary, join_dt, exit_dt in employees:
                if desig_id not in struct_by_designation:
                    continue

                # Active in month?
                if m_end < join_dt:
                    continue
                if exit_dt and m_start > exit_dt:
                    continue

                present_days = attendance_present.get(emp_id, 0)
                if present_days <= 0:
                    # No payroll if never present in the month
                    continue

                hra_pct, da_pct, allow_pct = struct_by_designation[desig_id]

                base = float(base_salary)
                hra = round(base * hra_pct / 100.0, 2)
                da = round(base * da_pct / 100.0, 2)
                allow = round(base * allow_pct / 100.0, 2)
                gross = round(base + hra + da + allow, 2)
                pf, tax, prof_tax = compute_deductions(gross)
                net = round(gross - (pf + tax + prof_tax), 2)

                ym_date = date(year, month, 1)
                batch.append(
                    (
                        emp_id,
                        ym_date,
                        base,
                        hra,
                        da,
                        allow,
                        gross,
                        pf,
                        tax,
                        prof_tax,
                        net,
                    )
                )

                if len(batch) >= batch_size:
                    execute_batch(
                        cur,
                        """
						INSERT INTO payroll_monthly(
							employee_id, year_month,
							base_salary, hra_amount, da_amount, allowance_amt,
							gross_salary, pf_deduction, tax_deduction,
							prof_tax, net_salary
						)
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
						ON CONFLICT (employee_id, year_month) DO NOTHING
						""",
                        batch,
                    )
                    conn.commit()
                    batch.clear()

        if batch:
            execute_batch(
                cur,
                """
				INSERT INTO payroll_monthly(
					employee_id, year_month,
					base_salary, hra_amount, da_amount, allowance_amt,
					gross_salary, pf_deduction, tax_deduction,
					prof_tax, net_salary
				)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
				ON CONFLICT (employee_id, year_month) DO NOTHING
				""",
                batch,
            )
            conn.commit()


def validate_data(conn) -> None:
    """Basic validation checks:

    - salary breakup sums (base + components == gross)
    - employee-month consistency (only for active employees)
    - FK-like integrity via join counts
    """

    with conn.cursor() as cur:
        # 1) salary breakup check
        cur.execute(
            """
			SELECT COUNT(*)
			FROM payroll_monthly
			WHERE ROUND(base_salary + hra_amount + da_amount + allowance_amt, 2)
				  != ROUND(gross_salary, 2)
			"""
        )
        mismatches = cur.fetchone()[0]

        # 2) employee-month: payroll only for employees existing at that month
        cur.execute(
            """
			SELECT COUNT(*)
			FROM payroll_monthly p
			JOIN employee e ON p.employee_id = e.employee_id
			WHERE (p.year_month < e.join_date)
			   OR (e.exit_date IS NOT NULL AND p.year_month > e.exit_date)
			"""
        )
        invalid_emp_month = cur.fetchone()[0]

        # 3) FK-like integrity: any payroll rows with missing employee?
        cur.execute(
            """
			SELECT COUNT(*)
			FROM payroll_monthly p
			LEFT JOIN employee e ON p.employee_id = e.employee_id
			WHERE e.employee_id IS NULL
			"""
        )
        orphan_payroll = cur.fetchone()[0]

    print("Validation Report:")
    print(f"  Payroll rows with inconsistent gross totals: {mismatches}")
    print(f"  Payroll rows with invalid employee-month: {invalid_emp_month}")
    print(f"  Payroll rows with missing employee FK: {orphan_payroll}")


def main():
    conn = get_connection()
    try:
        create_schema(conn)
        seed_master_data(conn)
        generate_employees(conn)
        generate_attendance(conn)
        generate_monthly_payroll(conn)
        validate_data(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
