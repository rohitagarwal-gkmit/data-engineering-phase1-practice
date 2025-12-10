# **Mini Expense Tracker CLI + Data Cleaner**

A tiny tool that helps you **record daily expenses**, fetch **currency conversion rates from an API**, store data with **Pandas**, and run fully via **Docker**, while letting you practice **Git workflow** and **environment setup**.

# 🧱 **High-Level Overview of the Project**

You build a CLI tool that supports:

### **1. Add an expense**

User inputs:

- amount
- category
- description
- currency (INR, USD, etc.)

### **2. Convert expenses to a base currency**

Using an API (e.g., ExchangeRate API):

- Fetch latest conversion rate
- Convert all expenses into INR

### **3. Store all expenses in a CSV file**

Pandas handles:

- reading
- writing
- appending
- cleaning

### **4. Clean & summarize expenses**

Examples:

- remove invalid rows
- calculate total per category
- show monthly spending summary

### **5. Run the whole app in Docker**

---

# 🗂️ **Suggested project structure**

```
expense-tracker/
    src/
        cli.py
        tracker/
            models/
            storage/
            converters/
    data/
    tests/
    docker/
    README.md
```

---

# 🏗️ **Breakdown of what you will build (step-by-step guidance)**

No code — just what you will **think about** and implement.

## **Build the CLI structure**

The CLI may support:

```
1. Add expense
2. View expenses
3. Convert currency
4. View summary
5. Exit
```

Focus on:

- functions
- input validation
- file interactions

---

## **Build a Pydantic model**

Model an “Expense” with:

- amount
- currency
- category
- timestamp

Validate:

- amount is numeric
- category is string
- currency is supported

This will break on Python 3.2 → good learning.

---

## **Implement Storage Layer Using Pandas**

- Append new expenses to a CSV
- Load CSV into DataFrame
- Clean data
- Handle duplicates

Focus on thinking about:

- DataFrame operations
- File paths
- Error handling

---

## **Use an API for currency conversion**

Steps you’ll think through:

- Call currency API
- Extract INR → USD or vice versa
- Apply conversion on Pandas DataFrame
- Save results back

---

## **summary functions**

Examples:

- total spending
- spending by category
- highest expense
- average spend per day

Use Pandas groupby + aggregates.

# **pytest tests**

Basic tests like:

- validating an expense model
- loading/saving CSV
