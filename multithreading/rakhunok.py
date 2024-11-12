import threading


class Rakhunok:
    def __init__(self, account_id: str, initial_balance: float = 0):
        self.account_id = account_id
        self.balance = initial_balance
        self._lock = threading.Lock()

    def deposit(self, amount: float) -> bool:
        with self._lock:
            if amount > 0:
                self.balance += amount
                print(f"    Rakhunok {self.account_id}: Popovneno {amount} grn. Balans: {self.balance} grn")
                return True
            return False

    def withdraw(self, amount: float) -> bool:
        with self._lock:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"    Rakhunok {self.account_id}: Vydano {amount} grn. Balans: {self.balance} grn")
                return True
            else:
                print(f"    Rakhunok {self.account_id}: Ne dostatno koshtiv na rakhunku.")
                return False

    def get_balance(self) -> float:
        with self._lock:
            return self.balance
