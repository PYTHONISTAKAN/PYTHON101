class TransactionManager:
    def __init__(self):
        self.transaction_history = []

    def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return False

        if from_account.balance < amount:
            print("Insufficient balance. Transfer cancelled.")
            return False

        from_account.withdraw(amount)
        to_account.deposit(amount)

        self.transaction_history.append(
            f"{from_account.owner.name} ({from_account.account_number}) → "
            f"{to_account.owner.name} ({to_account.account_number}) : {amount} USD"
        )

        print("Transfer successful.")
        return True

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if not self.transaction_history:
            print("No transactions have been made yet.")
        for tx in self.transaction_history:
            print(tx)
