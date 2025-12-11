from src.cli.main_menu import MainMenu
from src.utils.config import Config


def main() -> None:
    """Entry point for the Expense Tracker application."""

    print("Welcome to the Expense Tracker Application!")
    MainMenu()


def dev_entrypoints() -> None:
    """Development entry point for testing purposes."""

    print("Development Entry Point for Expense Tracker")
    Config()
