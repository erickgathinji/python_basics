# bank scenario
# data name, phone, gender, amount
# Account
# deposit / withdrawal / check balance
# object-oriented programming

# make sure all functions are in the same line
class Account:
    def __init__(self, full_name, acc_num, phone, balance):  # [special method/constructor - sets up info] - init = initialize def= define
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount): #define deposits
        self.balance += amount #self.balance is the current balance
        print(f"Amount ${amount} deposited successfully to account {self.acc_num}") #formatted

    def withdraw(self, amount): #define withdrawals to prevent overdrafts
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f'Amount {amount} withdrawn successfully from account {self.acc_num}')

    def check_balance(self):
        print(f"Balance for account {self.acc_num} is: ${self.balance}")
