from bankomat import Bankomat
import random
import time


def user_session(bankomat: Bankomat, account_id: str, num_operations: int):
    account = bankomat.get_account(account_id)
    if not account:
        return "Rakhunok ne znaideno"

    for _ in range(num_operations):
        operation = random.choice(['popovnennia', 'vudacha'])
        amount = random.randint(10, 100)

        if operation == 'popovnennia':
            account.deposit(amount)
        else:
            account.withdraw(amount)

        time.sleep(random.uniform(0.1, 0.5))
