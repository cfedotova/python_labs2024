from rakhunok import Rakhunok
from typing import Dict


class Bankomat:
    def __init__(self):
        self.accounts: Dict[str, Rakhunok] = {}

    def create_account(self, account_id: str, initial_balance: float = 0) -> Rakhunok:
        if account_id not in self.accounts:
            self.accounts[account_id] = Rakhunok(account_id, initial_balance)
        return self.accounts[account_id]

    def get_account(self, account_id: str) -> Rakhunok:
        return self.accounts.get(account_id)
