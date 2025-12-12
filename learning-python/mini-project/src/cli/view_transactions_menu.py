from src.services.transaction_service import TransactionService


class ViewTransactionsMenu:
    """Menu for viewing transaction records."""

    def __init__(self) -> None:
        """Initializes the ViewTransactionsMenu and displays transactions."""
        self.transaction_service = TransactionService()
        self.view_transactions()

    def view_transactions(self) -> None:
        """Displays all transactions."""
        print("\nView Transactions")

        transactions = self.transaction_service.get_transactions()

        if not transactions:
            print("No transactions found.")
            return

        print(f"Total transactions: {len(transactions)}")
        print("-" * 80)
        print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 80)

        for t in transactions:
            print(
                f"{t['id']:<5} {t['date']:<12} {t['category']:<15} {t['amount']:<10.2f} {t['description']}"
            )

        print("-" * 80)
