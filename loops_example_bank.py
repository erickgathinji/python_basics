# bank scenario
# data name, phone, gender, amount
# Account
# deposit / withdrawal / check balance
# object-oriented programming

# make sure all functions are in the same line
#don't quote amount
#self is like the object
class Account:
    def __init__(self, full_name, acc_num, phone, balance):  # [special method/constructor - sets up info] - init = initialize def= define
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount): #define deposits
        self.balance += amount #self.balance is the current balance
        print(f"Amount {amount} deposited successfully to account {self.acc_num}") #formatted

    def withdraw(self, amount): #define withdrawals to prevent overdrafts
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f'Amount {amount} withdrawn successfully from account {self.acc_num}')

    def check_balance(self):
        print(f"Balance for account {self.acc_num} is: {self.balance}")

#Create an Account now- outside the class - The Account calls the constructor created above
#follow same order as in the constructor otherwise do like in willy

willy_account = Account(balance=9000, full_name="Willy Kim", phone="555-555-5555", acc_num="0003")
kevo_acc = Account("Kevo Kim", "0001", "0712345678", 10000)
sara_acc = Account ("Sara Kim", "0002", "0712543567", 20000)
kevo_acc.deposit(1000)
kevo_acc.check_balance()
sara_acc.withdraw(1000)
sara_acc.check_balance()
willy_account.withdraw(1000)
willy_account.check_balance()