from src.services.transaction_service import TransactionService


class ViewSummaryMenu:
    """Menu for viewing transaction summary."""

    def __init__(self) -> None:
        """Initializes the ViewSummaryMenu and displays summary."""
        self.transaction_service = TransactionService()
        self.view_summary()

    def view_summary(self) -> None:
        """Displays transaction summary."""
        print("\nTransaction Summary")

        summary = self.transaction_service.get_summary()

        if summary["count"] == 0:
            print("No transactions found.")
            return

        print(f"Total Transactions: {summary['count']}")
        print(f"Total Amount: {summary['total']:.2f}")
        print("\nBreakdown by Category:")
        print("-" * 30)

        for category, amount in summary["by_category"].items():
            print(f"{category:<15}: {amount:.2f}")

        print("-" * 30)
