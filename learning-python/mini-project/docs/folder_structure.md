# Project Folder Structure

```
expense-tracker/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── commands.py
│   │   └── menu.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transaction.py
│   │   ├── settings.py
│   │   └── enums.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── transaction_service.py
│   │   ├── currency_converter.py
│   │   └── summary_service.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── storage_manager.py
│   │   └── csv_handler.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings_manager.py
│   │   └── constants.py
│   └── utils/
│       ├── __init__.py
│       ├── validators.py
│       ├── formatters.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   ├── test_transaction.py
│   │   └── test_settings.py
│   ├── test_services/
│   │   ├── __init__.py
│   │   ├── test_transaction_service.py
│   │   ├── test_currency_converter.py
│   │   └── test_summary_service.py
│   ├── test_storage/
│   │   ├── __init__.py
│   │   └── test_storage_manager.py
│   └── test_cli/
│       ├── __init__.py
│       └── test_commands.py
├── data/
│   ├── .gitkeep
│   └── expenses.csv
├── config/
│   ├── .gitkeep
│   └── settings.json
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── usage.md
├── .env.example
├── .gitignore
├── .python-version
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── pytest.ini
├── mypy.ini
├── .pylintrc
└── README.md
```
