class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #Public
        self.__balance = initial_deposit #Hide amount in outside (Private)
        self.branch = 'Banani' #Protected
 
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
        else:
            return f'Forkira taka nai'

rafsan = Bank('Choto bro', 10000)

print(rafsan.holder_name)
rafsan.deposit(40000)
print(rafsan.get_balance())

# Jor koira private attribute dekhar way:
print(dir(rafsan)) #Then find your attribute
print(rafsan._Bank__balance)