import csv
from pathlib import Path
from src.services.transaction_service import TransactionService


class ExportImportMenu:
    """Menu for exporting and importing transaction data."""

    def __init__(self) -> None:
        """Initializes the ExportImportMenu and displays options."""
        self.transaction_service = TransactionService()
        while True:
            self.show_menu()
            choice = self.get_user_choice()
            if not self.execute_choice(choice):
                break

    def show_menu(self) -> None:
        """Displays the export/import menu options."""
        print("\nExport/Import Data Menu:")
        print("1. Export to CSV")
        print("2. Import from CSV")
        print("3. Back to Main Menu")

    def get_user_choice(self) -> int:
        """Gets the user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in range(1, 4):
                    return choice
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, choice: int) -> bool:
        """Executes the action based on the user's choice."""
        if choice == 1:
            self.export_to_csv()
            return True
        elif choice == 2:
            self.import_from_csv()
            return True
        elif choice == 3:
            return False

    def export_to_csv(self) -> None:
        """Exports transactions to CSV file."""
        transactions = self.transaction_service.get_transactions()

        if not transactions:
            print("No transactions to export.")
            return

        file_path = (
            Path(__file__).parent.parent.parent / "data" / "exported_transactions.csv"
        )

        with open(file_path, "w", newline="") as csvfile:
            fieldnames = ["id", "amount", "category", "description", "date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)

        print(f"Transactions exported to {file_path}")

    def import_from_csv(self) -> None:
        """Imports transactions from CSV file."""
        file_path = (
            Path(__file__).parent.parent.parent / "data" / "exported_transactions.csv"
        )

        if not file_path.exists():
            print("No CSV file found to import.")
            return

        try:
            with open(file_path, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                transactions = list(reader)

            # Convert amount to float
            for t in transactions:
                t["amount"] = float(t["amount"])
                t["id"] = int(t["id"])

            # Save to data file
            self.transaction_service.save_transactions(transactions)
            print(f"Imported {len(transactions)} transactions from CSV.")

        except Exception as e:
            print(f"Error importing CSV: {e}")
