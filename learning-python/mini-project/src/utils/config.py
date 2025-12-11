import json
from pathlib import Path
from tkinter import N
from typing import Any


class Config:
    """Configuration class to manage application settings."""

    # absolute path to settings.json
    settings_file_rel_path = "../../config/settings.json"
    settings_file_abs_path = (
        Path(__file__).parent.parent.parent / "config" / "settings.json"
    )

    app_info: dict
    default_settings: dict
    supported_currencies: list
    user_preferences: dict
    user_details: dict

    def __init__(self):
        """Initializes the Config class with default settings."""

        with open(self.settings_file_abs_path, "r") as file:
            data = json.load(file)
            self.app_info = data.get("app_info", {})
            self.default_settings = data.get("default_settings", {})
            self.supported_currencies = data.get("supported_currencies", [])
            self.user_preferences = data.get("user_preferences", {})
            self.user_details = data.get("user_details", {})

    def change_setting(self, setting_key: str, setting_value: Any) -> None:
        """Changes a specific setting in the configuration.

        Args:
            setting_key (str): The key of the setting to change.
            setting_value: The new value for the setting.
        """

        if setting_key in self.default_settings:
            self.default_settings[setting_key] = setting_value
            print(f"Setting '{setting_key}' updated to {setting_value}.")

        else:
            print(f"Setting '{setting_key}' not found in default settings.")

    def initial_setup(self) -> None:
        """Performs initial setup for the user."""

        print("Performing initial setup...")
        print("Hello What is your name?")

        name = input()

        while True:
            print("You Typed - ", name)

            print("Is your Name Correct? Continue -  Yes/No")
            confirmation = input().strip().lower()

            if confirmation == "no":
                name = input("Enter your name: ")
                continue
            else:
                break

        print("Select your preferred currency from the following options:")
        for currency in self.supported_currencies:
            print(f"- {currency}")

        currency = input("Enter your preferred currency: ").strip().upper()

        # validate currency input
        while currency not in self.supported_currencies:
            print(
                f"Currency '{currency}' is not supported. Please choose from {self.supported_currencies}."
            )
            currency = input("Enter your preferred currency: ").strip().upper()

        while True:
            print("You Selected - ", currency)

            print("Is this correct? Continue - Yes/No")
            currency_confirmation = input().strip().lower()

            if currency_confirmation == "no":
                currency = input("Enter your preferred currency: ").strip().upper()
                continue
            else:
                break

        self.user_details["name"] = name
        if currency in self.supported_currencies:
            self.user_preferences["currency"] = currency
            print(f"User '{name}' setup with preferred currency '{currency}'.")

            with open(self.settings_file_abs_path, "r+") as file:
                data = json.load(file)
                data["user_details"] = self.user_details
                data["user_preferences"] = self.user_preferences
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
        else:
            print(
                f"Currency '{currency}' is not supported. Please choose from {self.supported_currencies}."
            )

    def setup_checker(self, func):
        def check_initial_setup_complete(*args, **kwargs) -> None:
            """
            Checks if the initial setup is complete. If not, it triggers the initial setup process.
            """

            name = self.user_details.get("name", "")
            currency = self.user_preferences.get("currency", "")

            if name and currency:
                return func(*args, **kwargs)
            else:
                self.initial_setup()
                return func(*args, **kwargs)

        return check_initial_setup_complete
