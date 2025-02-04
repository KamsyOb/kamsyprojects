# Define a class for a bank account
class BankAccount:
    def __init__(self, account_holder, balance=0):
        """
        Initialize a new bank account.
        :param account_holder: The name of the account holder.
        :param balance: Initial balance (default is 0).
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :param amount: Amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def __str__(self):
        """
        Return a string representation of the account.
        """
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"


# Example usage
if __name__ == "__main__":
    # Create a new bank account for "Alice"
    alice_account = BankAccount("Alice", 100)

    # Display account details
    print(alice_account)

    # Deposit money
    alice_account.deposit(50)

    # Withdraw money
    alice_account.withdraw(30)

    # Attempt to withdraw more than the balance
    alice_account.withdraw(150)

    # Display final account details
    print(alice_account)
