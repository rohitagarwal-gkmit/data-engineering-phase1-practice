## One-line steps: Realistic OLTP data generation (PostgreSQL)

1. Design master tables for departments, designations, and salary structures with HRA/DA/allowance percentages.
2. Map each designation to a salary structure defining fixed percentage breakdowns.
3. Create employee records with designation, department, base salary, join date, and optional exit date.
4. Ensure salary structure percentages remain constant for a designation (simulate HR policy).
5. Generate daily attendance records only for active employees and valid working days.
6. Generate monthly payroll records by computing salary components from base salary + structure percentages.
7. Apply deductions (PF, tax, professional tax) as deterministic or rule-based values.
8. Insert payroll records only for months where the employee was active and present.
9. Insert data in large batches with periodic commits to simulate production write patterns.
10. Validate totals (salary breakup sums, employee-month consistency, FK integrity).
