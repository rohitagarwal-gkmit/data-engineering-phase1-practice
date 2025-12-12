import json
from pathlib import Path
from src.services.transaction_service import TransactionService
from src.utils.config import Config


class AddRecordMenu:
    """Menu for adding new transaction records."""

    def __init__(self) -> None:
        """Initializes the AddRecordMenu and handles adding a record."""
        self.transaction_service = TransactionService()
        self.config = Config()
        self.add_record()

    def add_record(self) -> None:
        """Prompts user for transaction details and adds the record."""
        print("\nAdd New Transaction Record")

        # Get amount
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        # Get category
        categories = self.config.app_info.get("categories", [])
        if not categories:
            # Load from categories.json if not in config
            try:
                with open(
                    Path(__file__).parent.parent.parent / "config" / "categories.json",
                    "r",
                ) as f:
                    categories = json.load(f).get("categories", [])
            except Exception:
                categories = [
                    "FOOD",
                    "TRANSPORT",
                    "SALARY",
                    "ENTERTAINMENT",
                    "UTILITIES",
                    "HEALTHCARE",
                    "OTHER",
                ]

        print("Available categories:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        while True:
            try:
                cat_choice = int(input(f"Select category (1-{len(categories)}): "))
                if 1 <= cat_choice <= len(categories):
                    category = categories[cat_choice - 1]
                    break
                else:
                    print(f"Invalid choice. Please select 1-{len(categories)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get description
        description = input("Enter description: ").strip()
        while not description:
            description = input(
                "Description cannot be empty. Enter description: "
            ).strip()

        # Get date (optional)
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date:
            date = None

        # Add transaction
        self.transaction_service.add_transaction(amount, category, description, date)
        print("Transaction added successfully!")
