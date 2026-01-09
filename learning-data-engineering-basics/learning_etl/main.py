import duckdb


def create_tables(conn: duckdb.DuckDBPyConnection):
    conn.execute("DROP TABLE IF EXISTS attendance")
    conn.execute("DROP TABLE IF EXISTS payroll_monthly")
    conn.execute("DROP TABLE IF EXISTS employee")
    conn.execute("DROP TABLE IF EXISTS designation")
    conn.execute("DROP TABLE IF EXISTS salary_structure")
    conn.execute("DROP TABLE IF EXISTS department")

    # department
    conn.execute("""
        CREATE TABLE department (
            department_id INTEGER,
            name TEXT
        );
    """)

    # salary_structure
    conn.execute("""
        CREATE TABLE salary_structure (
            structure_id INTEGER,
            code TEXT,
            hra_pct DOUBLE,
            da_pct DOUBLE,
            allowance_pct DOUBLE
        );
    """)

    # designation
    conn.execute("""
        CREATE TABLE designation (
            designation_id INTEGER,
            title TEXT,
            structure_id INTEGER
        );
    """)

    # employee
    conn.execute("""
        CREATE TABLE employee (
            employee_id INTEGER,
            full_name TEXT,
            department_id INTEGER,
            designation_id INTEGER,
            base_salary DOUBLE,
            join_date DATE,
            exit_date DATE
        );
    """)

    # payroll_monthly
    conn.execute("""
        CREATE TABLE payroll_monthly (
            payroll_id INTEGER,
            employee_id INTEGER,
            year_month DATE,
            base_salary DOUBLE,
            hra_amount DOUBLE,
            da_amount DOUBLE,
            allowance_amt DOUBLE,
            gross_salary DOUBLE,
            pf_deduction DOUBLE,
            tax_deduction DOUBLE,
            prof_tax DOUBLE,
            net_salary DOUBLE
        );
    """)

    # attendance
    conn.execute("""
        CREATE TABLE attendance (
            attendance_id INTEGER,
            employee_id INTEGER,
            att_date DATE,
            status TEXT
        );
    """)


def load_data(conn: duckdb.DuckDBPyConnection):
    conn.execute("""
        COPY department FROM 'raw_data/department.csv' (AUTO_DETECT TRUE);
        COPY salary_structure FROM 'raw_data/salary_structure.csv' (AUTO_DETECT TRUE);
        COPY designation FROM 'raw_data/designation.csv' (AUTO_DETECT TRUE);
        COPY employee FROM 'raw_data/employee.csv' (AUTO_DETECT TRUE);
        COPY payroll_monthly FROM 'raw_data/payroll_monthly.csv' (AUTO_DETECT TRUE);
        COPY attendance FROM 'raw_data/attendance_part1.csv' (AUTO_DETECT TRUE);
        COPY attendance FROM 'raw_data/attendance_part2.csv' (AUTO_DETECT TRUE);
        COPY attendance FROM 'raw_data/attendance_part3.csv' (AUTO_DETECT TRUE);""")


def check_data(conn: duckdb.DuckDBPyConnection):
    result = conn.execute("SELECT COUNT(*) FROM employee;").fetchone()
    print(f"Total employees: {result}")


if __name__ == "__main__":
    conn = duckdb.connect(database="warehouse.test_db", read_only=False)
    create_tables(conn)
    load_data(conn)
    check_data(conn)
    conn.close()
