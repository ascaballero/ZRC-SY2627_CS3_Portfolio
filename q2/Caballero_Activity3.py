
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0.0
        self.set_balance(balance)

    # Setter for account number
    def set_account_number(self, account_number):
        self.__account_number = account_number

    # Setter for balance with validation
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = float(balance)
        else:
            print("The balance must not be a negative number.")

    # Getter for account number
    @property
    def account_number(self):
        return self.__account_number

    # Getter for balance
    @property
    def balance(self):
        return self.__balance


# Testing the BankAccount class
print("Object of class BankAccount")

a1 = BankAccount(12345, 1000)

print("\nOutput:")
print("Account 1")
print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100)

print(f"Account Number: {a1.account_number}")
print(f"Balance: {a1.balance:.2f}")
