class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


my_phone = Phone('John', 'Apple', 130000)
her_phone = Phone('Smith', 'Samsung', 120000)
your_phone = Phone('Jeff', 'Xiaomi', 70000)

print(my_phone.owner, my_phone.brand, my_phone.price)
print(her_phone.owner, her_phone.brand, her_phone.price)
print(your_phone.owner, your_phone.brand, your_phone.price)