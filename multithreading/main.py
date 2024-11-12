import threading
from bankomat import Bankomat
from sesssion import user_session


def main():
    atm = Bankomat()

    accounts = [
        ('Petrenko Ivan', 1000),
        ('Tysiak Vasyl', 1500),
        ('Sadovyi Andrii', 200000),
        ('Kliveta Andriy', 50)
    ]

    for acc_id, initial_balance in accounts:
        atm.create_account(acc_id, initial_balance)

    threads = []
    for acc_id, _ in accounts:
        thread = threading.Thread(
            target=user_session,
            args=(atm, acc_id, 3)
        )
        threads.append(thread)

    print("\nPochatkovyi balans:")
    for acc_id in atm.accounts:
        account = atm.get_account(acc_id)
        print(f"    Rakhunok {acc_id}: {account.get_balance()} grn")

    print("Pochatok operacii...")
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("\nKincevyi balans:")
    for acc_id in atm.accounts:
        account = atm.get_account(acc_id)
        print(f"    Rakhunok {acc_id}: {account.get_balance()} grn")


if __name__ == "__main__":
    main()
