from user import User
from account import Account

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.accounts = []

    def create_user(self, name, email, password):
        user = User(name, email, password)
        self.users.append(user)
        print(f"User created: {name} (ID: {user.id})")
        return user

    def create_account_for_user(self, user: User, initial_balance=0):
        account = Account(owner=user, initial_balance=initial_balance)
        self.accounts.append(account)
        print(f"Account created (Account No: {account.account_number})")
        return account

    def get_accounts_by_user(self, user: User):
        user_accounts = [acc for acc in self.accounts if acc.owner == user]
        return user_accounts

    def show_all_users(self):
        print("\n--- User List ---")
        for user in self.users:
            user.display_info()

    def show_user_accounts(self, user: User):
        print(f"\n--- Accounts of {user.name} ---")
        accounts = self.get_accounts_by_user(user)
        if not accounts:
            print("No accounts found for this user.")
        for account in accounts:
            account.display_account_info()
