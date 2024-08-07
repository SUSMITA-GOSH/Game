class Account:
    def __init__(self, bal, acc,password):
        self.bal = bal
        self.acc = acc
        self.__password=password

    @staticmethod
    def welcome():
        print("Welcome ....")
        
    def reset_password(self):
        print(self.__password)
    
    def debit(self, amount):
        print("Account No: ",self.acc)
        self.bal -= amount
        print("Tk " + str(amount) + " is debited")
        print("Your total balance:", self.get_balance())

    def credit(self, amount):
        self.bal += amount
        print("Tk " + str(amount) + " is credited")
        print("Your total balance:", self.get_balance())

    def get_balance(self):
        return self.bal

# Creating an instance of the Account class
acc1 = Account(10000000, 78578,45678)

# Calling the static method
Account.welcome()

# Performing debit and credit operations
acc1.debit(10000)
acc1.credit(2946)
#print(acc1.__password) we can't access it
print(acc1.reset_password())