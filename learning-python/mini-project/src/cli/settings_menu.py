class SettingsMenu:
    def __init__(self) -> None:
        """Initializes the SettingsMenu class and displays the menu."""
        while True:
            self.show_settings_menu()
            choice = self.get_user_choice()
            if not self.execute_choice(choice):
                break

    def show_settings_menu(self) -> None:
        """Displays the settings menu options to the user."""

        print("\nSettings Menu:")
        print("1. Change User Name")
        print("2. Change Preferred Currency")
        print("3. Back to Main Menu")

    def get_user_choice(self) -> int:
        """Gets the user's settings menu choice.

        Returns:
            int: The user's choice as an integer.
        """

        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in range(1, 4):
                    return choice
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, choice: int) -> None:
        """Executes the action based on the user's settings menu choice.

        Args:
            choice (int): The user's menu choice.
        """

        if choice == 1:
            print("Change User Name selected.")
            # TODO: Implement name change logic
            return True
        elif choice == 2:
            print("Change Preferred Currency selected.")
            # TODO: Implement currency change logic
            return True
        elif choice == 3:
            print("Returning to Main Menu...")
            return False
        else:
            print("Invalid choice.")
            return True
