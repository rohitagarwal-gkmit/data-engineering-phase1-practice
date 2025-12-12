import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
from src.utils.config import Config


class TransactionService:
    """Service class to handle transaction operations."""

    def __init__(self):
        self.config = Config()
        self.data_file_path = Path(
            __file__
        ).parent.parent.parent / self.config.default_settings.get(
            "data_file_path", "data/transactions.json"
        )
        self.data_file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file_path.exists():
            with open(self.data_file_path, "w") as f:
                json.dump([], f)

    def load_transactions(self) -> List[Dict[str, Any]]:
        """Loads transactions from the data file."""
        try:
            with open(self.data_file_path, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self, transactions: List[Dict[str, Any]]) -> None:
        """Saves transactions to the data file."""
        with open(self.data_file_path, "w") as f:
            json.dump(transactions, f, indent=4)

    def add_transaction(
        self, amount: float, category: str, description: str, date: str = None
    ) -> None:
        """Adds a new transaction."""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        transaction = {
            "id": len(self.load_transactions()) + 1,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date,
        }
        transactions = self.load_transactions()
        transactions.append(transaction)
        self.save_transactions(transactions)

    def get_transactions(self) -> List[Dict[str, Any]]:
        """Gets all transactions."""
        return self.load_transactions()

    def get_summary(self) -> Dict[str, Any]:
        """Gets a summary of transactions."""
        transactions = self.load_transactions()
        total = sum(t["amount"] for t in transactions)
        by_category = {}
        for t in transactions:
            cat = t["category"]
            by_category[cat] = by_category.get(cat, 0) + t["amount"]
        return {"total": total, "by_category": by_category, "count": len(transactions)}
