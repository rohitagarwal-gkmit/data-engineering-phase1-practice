class MainMenu(is_setup_complete=None):
    """Class to represent the menu options in the Expense Tracker CLI."""

    # if inital setup is not complete, do not show menu, redirect to setup
    if is_setup_complete is False:
        from src.cli.setup import Setup

        Setup()
        return

    ADD_INCOME = 1
    ADD_EXPENSE = 2
    VIEW_TRANSACTIONS = 3
    VIEW_SUMMARY = 4
    EXPORT_IMPORT = 5
    CURRENCY_CONVERTOR = 6
    SETTINGS = 7
    EXIT = 8

    user_choice = None

    def __init__(self) -> None:
        """Initializes the MainMenu class and displays the menu."""

        self.show_menu()
        choice = self.get_user_choice()
        self.execute_choice(choice)

    def show_menu(self) -> None:
        """Displays the menu options to the user."""

        print("\nExpense Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Export/Import Data")
        print("6. Currency Convertor")
        print("7. Settings")
        print("8. Exit")

    def get_user_choice() -> int:
        """Gets the user's menu choice.

        Returns:
            int: The user's choice as an integer.
        """

        try:
            choice = int(input("Enter your choice (1-8): "))
            if choice in range(1, 9):
                MainMenu.user_choice = choice
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 8.")
                return MainMenu.get_user_choice()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return MainMenu.get_user_choice()

    def execute_choice(self, choice: int) -> None:
        """Executes the action based on the user's choice.

        Args:
            choice (int): The user's menu choice.
        """

        if choice == MainMenu.ADD_INCOME:
            print("Add Income selected.")
            # Call function to add income
        elif choice == MainMenu.ADD_EXPENSE:
            print("Add Expense selected.")
            # Call function to add expense
        elif choice == MainMenu.VIEW_TRANSACTIONS:
            print("View Transactions selected.")
            # Call function to view transactions
        elif choice == MainMenu.VIEW_SUMMARY:
            print("View Summary selected.")
            # Call function to view summary
        elif choice == MainMenu.EXPORT_IMPORT:
            print("Export/Import Data selected.")
            # Call function to export/import data
        elif choice == MainMenu.CURRENCY_CONVERTOR:
            print("Currency Convertor selected.")
            # Call function for currency conversion
        elif choice == MainMenu.SETTINGS:
            print("Settings selected.")
            # Call function to modify settings
        elif choice == MainMenu.EXIT:
            print("Exiting Expense Tracker. Goodbye!")
            exit()
