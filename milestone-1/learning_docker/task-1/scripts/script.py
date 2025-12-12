import csv
import random
from datetime import datetime, timedelta

# --- Configuration ---
header = ["user_id", "username", "email", "signup_date", "is_active"]
num_records = 60
output_filename = "user_data.csv"


# --- Data Generation Helper ---
def random_date(start_date):
    """Generates a random date within the last year."""
    return start_date - timedelta(days=random.randint(1, 365))


# --- Main Logic ---
data = []
start_date = datetime.now()

for i in range(1, num_records + 1):
    user_id = i
    username = f"user_{i:03d}"
    email = f"user{i}@example.com"
    signup_date = random_date(start_date).strftime("%Y-%m-%d")
    is_active = random.choice([True, False])

    data.append([user_id, username, email, signup_date, is_active])

# --- Write to CSV file ---
try:
    with open(output_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header
        writer.writerows(data)  # Write data rows

    print(f"✅ Successfully generated {num_records} records in {output_filename}")

except Exception as e:
    print(f"❌ An error occurred: {e}")
