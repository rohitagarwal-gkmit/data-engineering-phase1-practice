# Expense Tracker CLI - Development Tasks

## Project Setup

- [x] Create virtual environment using venv or pyenv
- [] Initialize .gitignore file for Python projects
- [x] Create requirements.txt file
- [] Set up folder structure as per project layout
- [] Initialize all **init**.py files in packages
- [] Set up logging configuration

## Data Models

- [] Create Enum for TransactionType (INCOME, EXPENSE)
- [] Create Enum for Currency (INR, USD, EUR, GBP, etc.)
- [] Create Enum for Category (FOOD, TRANSPORT, SALARY, etc.)
- [] Create Transaction model using Pydantic with validation
- [] Add type hints to all model fields
- [] Add validation for positive amounts
- [] Add validation for valid currencies
- [] Add timestamp generation
- [] Add unique ID generation for transactions

## Configuration & Settings

- [] Create Settings model using Pydantic
- [] Define config file location (~/.expense-tracker/config.json or local)
- [] Implement first-run detection logic
- [] Create default settings structure
- [] Build settings loader function
- [] Build settings saver function
- [] Implement first-run setup wizard for default currency
- [] Create settings update functions
- [] Add error handling for corrupt config files
- [] Add settings validation

## Storage Layer

- [] Design StorageManager/DataRepository class
- [] Implement CSV file creation on first run
- [] Implement add_transaction() method
- [] Implement get_all_transactions() method
- [] Implement get_transactions_by_filter() method
- [] Implement delete_transaction() method
- [] Implement update_transaction() method
- [] Add data validation when loading from CSV
- [] Add duplicate detection and removal
- [] Handle missing or corrupt CSV files
- [] Implement export_to_csv() method
- [] Implement import_from_csv() method
- [] Add data backup functionality
- [] Use Pathlib for all file operations

## Currency Conversion Service

- [] Research and choose currency API (ExchangeRate-API, Fixer.io)
- [] Create CurrencyConverter class
- [] Implement API call to fetch exchange rates
- [] Add error handling for network failures
- [] Add error handling for API rate limits
- [] Implement rate caching mechanism (in-memory or file)
- [] Set cache expiry time
- [] Implement convert_amount() method
- [] Implement get_exchange_rate() method
- [] Add offline mode handling
- [] Store API key in environment variable or config
- [] Add retry logic for failed API calls

## Summary & Analytics

- [] Create SummaryService class
- [] Implement calculate_total_income() method
- [] Implement calculate_total_expenses() method
- [] Implement calculate_net_balance() method
- [] Implement get_summary_by_category() method
- [] Implement get_summary_by_month() method
- [] Implement get_summary_by_date_range() method
- [] Use Pandas groupby for aggregations
- [] Add filtering options (by date, category, type)
- [] Format currency values for display
- [] Create visual representations (if using rich library)

## CLI Interface

- [] Choose CLI framework (Click, Typer, or argparse)
- [] Create main menu display
- [] Implement menu loop
- [] Create "Add Income" command/menu option
- [] Create "Add Expense" command/menu option
- [] Create "List All" command/menu option
- [] Create "Summary" command/menu option
- [] Create "Export" command/menu option
- [] Create "Import" command/menu option
- [] Create "Currency Converter" command/menu option
- [] Create "Settings" command/menu option
- [] Create "Exit" command/menu option
- [] Add input validation for all user inputs
- [] Add clear error messages
- [] Add success confirmation messages
- [] Implement pretty output formatting (consider rich library)
- [] Add help text for each command
- [] Handle keyboard interrupts gracefully (Ctrl+C)

## Business Logic

- [] Create TransactionService class
- [] Implement add_income() method with validation
- [] Implement add_expense() method with validation
- [] Implement list_transactions() with filtering
- [] Implement delete_transaction() method
- [] Implement update_transaction() method
- [] Add business rule validations
- [] Integrate with StorageManager
- [] Integrate with CurrencyConverter
- [] Integrate with SummaryService
- [] Add logging for all operations
- [] Handle edge cases (empty data, invalid dates, etc.)

## Testing

- [] Set up pytest configuration
- [] Create test fixtures for sample data
- [] Write unit tests for Transaction model validation
- [] Write unit tests for Settings model
- [] Write unit tests for StorageManager methods
- [] Write unit tests for CurrencyConverter (mock API)
- [] Write unit tests for SummaryService calculations
- [] Write unit tests for business logic
- [] Write integration tests for end-to-end workflows
- [] Write tests for file I/O operations
- [] Mock external API calls in tests
- [] Aim for >80% test coverage
- [] Run tests and fix failures

## Docker Setup

- [] Create Dockerfile with Python base image
- [] Copy requirements.txt and install dependencies
- [] Copy source code into container
- [] Set appropriate working directory
- [] Define entry point for CLI
- [] Set up volume mounting for data persistence
- [] Set up volume mounting for config files
- [] Build Docker image locally
- [] Test running container
- [] Add docker-compose.yml if needed
- [] Document Docker usage in README

## Documentation

- [] Add docstrings to all classes (Google/NumPy style)
- [] Add docstrings to all methods/functions
- [] Add type hints to all functions
- [] Add inline comments for complex logic
- [] Write comprehensive README with:
  - [] Project description
  - [] Features list
  - [] Installation instructions
  - [] Usage examples
  - [] Configuration guide
  - [] API documentation (if applicable)
  - [] Docker instructions
  - [] Testing instructions
  - [] Contributing guidelines
- [] Create usage examples
- [] Document folder structure
- [] Document design decisions

## Code Quality & Refinement

- [] Review all code for type hints
- [] Replace all print() with logging
- [] Extract magic numbers to constants
- [] Extract magic strings to constants
- [] Check for DRY violations
- [] Verify Single Responsibility Principle
- [] Add proper exception handling everywhere
- [] Use context managers for file operations
- [] Replace string paths with Pathlib
- [] Use f-strings for string formatting
- [] Review naming conventions (snake_case, PascalCase, UPPER_CASE)
- [] Ensure descriptive variable/function names
- [] Run linter (pylint, flake8, or ruff)
- [] Run type checker (mypy)
- [] Fix all linter warnings
- [] Fix all type checking errors
- [] Refactor duplicated code
- [] Optimize imports (remove unused)
- [] Format code with black or autopep8

## Final Review & Deployment

- [] Run all tests and ensure they pass
- [] Test all CLI commands manually
- [] Test first-run experience
- [] Test error scenarios
- [] Test with empty data
- [] Test with large datasets
- [] Test import/export functionality
- [] Test Docker container end-to-end
- [] Review README for accuracy
- [] Create release notes
- [] Tag version in git
- [] Push to repository
