from bank import Bank
from transaction import TransactionManager

# Create a bank
my_bank = Bank("Pinnacle Bank")

# Create users
user1 = my_bank.create_user("Atakan", "atakan@example.com", "1234")
user2 = my_bank.create_user("Zeynep", "zeynep@example.com", "abcd")

# Create accounts for users
acc1 = my_bank.create_account_for_user(user1, 1000)
acc2 = my_bank.create_account_for_user(user2, 500)

# Transaction manager
transaction_manager = TransactionManager()

# Show user accounts
my_bank.show_user_accounts(user1)
my_bank.show_user_accounts(user2)

# Transfer operation
print("\n--- Transfer in Progress ---")
transaction_manager.transfer(acc1, acc2, 300)  # Atakan to Zeynep 300 USD

# Show transaction history
transaction_manager.show_transactions()

# Display updated account details
my_bank.show_user_accounts(user1)
my_bank.show_user_accounts(user2)
