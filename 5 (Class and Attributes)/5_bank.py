class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print (f'Here is your updated money: {self.balance}')
        
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print (f'You can not withdraw less than {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'You can not withdraw more that {self.max_withdraw} in one time')
        else:
            self.balance -= amount
            print (f'Here is your updated money: {self.balance}')
        

bank_asia = Bank(15000)
bank_asia.withdraw(25)
bank_asia.withdraw(500)
bank_asia.withdraw(500000)
bank_asia.deposit(4500)

dbbl = Bank(5000)
dbbl.withdraw(35)
dbbl.withdraw(2000)
dbbl.withdraw(500000)
dbbl.deposit(6000)

