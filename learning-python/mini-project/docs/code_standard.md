Code Quality:
✅ Type hints on all functions
✅ Docstrings (Google/NumPy style)
✅ Single Responsibility Principle
✅ DRY (Don't Repeat Yourself)
✅ Error handling (try-except with specific exceptions)
✅ Logging instead of print statements
✅ Constants in UPPER_CASE
✅ No magic numbers/strings
Structure:
✅ Clear separation: models, services, storage, CLI, utils
✅ **init**.py in packages
✅ Relative imports within package
✅ Config separate from code
✅ Tests mirror src structure
Naming:
✅ snake_case for functions/variables
✅ PascalCase for classes
✅ UPPER_CASE for constants
✅ Descriptive names (avoid abbreviations)
✅ Verb functions, noun classes
Python-specific:
✅ Use context managers (with statements)
✅ List comprehensions where appropriate
✅ Pathlib for file paths (not string concatenation)
✅ F-strings for formatting
✅ Dataclasses/Pydantic for data structures
