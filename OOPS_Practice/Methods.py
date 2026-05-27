class BankAccount:
    
    counter = 1000
    
    @staticmethod
    def validate_pin(passkey):
        return passkey.isdigit() and len(passkey) == 4
    
    def __init__(self, name, balance, pin):
        
        if not self.validate_pin(pin):
            raise ValueError("set correct pin")
        self.name = name
        self.balance = balance 
        self.pin = pin 
        self.account_number = self.generate_acc_number()
    
    
    def deposit_money(self, amount):
        self.balance += amount
        print(f"{amount} added successfully")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"{amount} withdrawn successfully")
    
    
    def check_balance(self):
        return self.balance
    
    @classmethod
    def generate_acc_number(cls):
        cls.counter = cls.counter + 1
        return cls.counter


a1 = BankAccount("Pranav", 5000, "1234")
a2 = BankAccount("Rahul", 8000, "5678")

print(a1.account_number)
print(a2.account_number)

a1.deposit_money(1000)
print(a1.check_balance())
a1.withdraw_money(2000)

print(a1.check_balance())

print(BankAccount.validate_pin("9999"))
print(BankAccount.validate_pin("12a4"))