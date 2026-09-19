class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")

    # Display balance
    def display_balance(self):
        print(f"Current balance: ${self.__balance}")


# Create a bank account
account = BankAccount("Lawrence", 1000)

# Display initial balance
account.display_balance()

# Deposit money
account.deposit(500)

# Display balance
account.display_balance()

# Withdraw money
account.withdraw(300)

# Display final balance
account.display_balance()
