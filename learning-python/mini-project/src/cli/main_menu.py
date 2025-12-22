from src.utils.config import Config


class MainMenu:
    """Class to represent the menu options in the Expense Tracker CLI."""

    # if inital setup is not complete, do not show menu, redirect to setup

    ADD_RECORD = 1
    VIEW_TRANSACTIONS = 2
    VIEW_SUMMARY = 3
    EXPORT_IMPORT = 4
    CURRENCY_CONVERTOR = 5
    SETTINGS = 6
    EXIT = 7

    config = Config()

    @config.setup_checker
    def __init__(self) -> None:
        """Initializes the MainMenu class and displays the menu."""
        while True:
            self.show_menu()
            choice = self.get_user_choice()
            if not self.execute_choice(choice):
                break

    def show_menu(self) -> None:
        """Displays the menu options to the user."""

        print("\nExpense Tracker Menu:")
        print("1. Add Record")
        print("2. View Transactions")
        print("3. View Summary")
        print("4. Export/Import Data")
        print("5. Currency Convertor")
        print("6. Settings")
        print("7. Exit")

    def get_user_choice(self) -> int:
        """Gets the user's menu choice.

        Returns:
            int: The user's choice as an integer.
        """

        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if choice in range(1, 8):
                    return choice
                else:
                    print("Invalid choice. Please select a number between 1 and 7.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, choice: int) -> bool:
        """Executes the action based on the user's choice.

        Args:
            choice (int): The user's menu choice.
        """

        if choice == MainMenu.ADD_RECORD:
            from src.cli.add_record_menu import AddRecordMenu

            AddRecordMenu()
            return True

        elif choice == MainMenu.VIEW_TRANSACTIONS:
            from src.cli.view_transactions_menu import ViewTransactionsMenu

            ViewTransactionsMenu()
            return True

        elif choice == MainMenu.VIEW_SUMMARY:
            from src.cli.view_summary_menu import ViewSummaryMenu

            ViewSummaryMenu()
            return True

        elif choice == MainMenu.EXPORT_IMPORT:
            from src.cli.export_import_menu import ExportImportMenu

            ExportImportMenu()
            return True

        elif choice == MainMenu.CURRENCY_CONVERTOR:
            from src.cli.currency_convertor_menu import CurrencyConvertorMenu

            CurrencyConvertorMenu()
            return True

        elif choice == MainMenu.SETTINGS:
            from src.cli.settings_menu import SettingsMenu

            SettingsMenu()
            return True

        elif choice == MainMenu.EXIT:
            print("Exiting Expense Tracker. Goodbye!")
            return False
