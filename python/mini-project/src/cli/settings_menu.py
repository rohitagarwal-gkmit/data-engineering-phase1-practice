from .main_menu import MainMenu

main_menu = MainMenu()


class SettingsMenu:
    def __init__(self) -> None:
        """Initializes the SettingsMenu class and displays the settings menu."""

        self.show_settings_menu()
        choice = self.get_user_choice()
        self.execute_choice(choice)

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

        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in range(1, 4):
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 3.")
                return self.get_user_choice()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_user_choice()

    def execute_choice(self, choice: int) -> None:
        """Executes the action based on the user's settings menu choice.

        Args:
            choice (int): The user's menu choice.
        """

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            main_menu.__init__()()
        else:
            print("Invalid choice.")
            SettingsMenu.get_user_choice(self)
