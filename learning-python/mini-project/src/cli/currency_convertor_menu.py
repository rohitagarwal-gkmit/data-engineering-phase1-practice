from src.utils.config import Config


class CurrencyConvertorMenu:
    """Menu for currency conversion."""

    # Simple exchange rates (in real app, use API)
    EXCHANGE_RATES = {"USD": 1.0, "EUR": 0.85, "GBP": 0.73, "INR": 74.5}

    def __init__(self) -> None:
        """Initializes the CurrencyConvertorMenu and handles conversion."""
        self.config = Config()
        self.convert_currency()

    def convert_currency(self) -> None:
        """Prompts user for conversion details and performs conversion."""
        print("\nCurrency Convertor")

        supported_currencies = self.config.supported_currencies

        print("Supported currencies:", ", ".join(supported_currencies))

        # Get amount
        while True:
            try:
                amount = float(input("Enter amount to convert: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        # Get from currency
        print("Select source currency:")
        for i, curr in enumerate(supported_currencies, 1):
            print(f"{i}. {curr}")

        while True:
            try:
                from_choice = int(
                    input(f"Select source currency (1-{len(supported_currencies)}): ")
                )
                if 1 <= from_choice <= len(supported_currencies):
                    from_currency = supported_currencies[from_choice - 1]
                    break
                else:
                    print(
                        f"Invalid choice. Please select 1-{len(supported_currencies)}."
                    )
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Get to currency
        print("Select target currency:")
        for i, curr in enumerate(supported_currencies, 1):
            print(f"{i}. {curr}")

        while True:
            try:
                to_choice = int(
                    input(f"Select target currency (1-{len(supported_currencies)}): ")
                )
                if 1 <= to_choice <= len(supported_currencies):
                    to_currency = supported_currencies[to_choice - 1]
                    break
                else:
                    print(
                        f"Invalid choice. Please select 1-{len(supported_currencies)}."
                    )
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Perform conversion
        converted_amount = self.convert(amount, from_currency, to_currency)
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Converts amount from one currency to another."""
        # Convert to USD first, then to target currency
        usd_amount = amount / self.EXCHANGE_RATES[from_currency]
        return usd_amount * self.EXCHANGE_RATES[to_currency]
