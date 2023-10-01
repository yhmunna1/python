class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'Item': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)

    def check_out(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['Price'] * item['Quantity']
        print('Total price', total)
        if amount < total:
            need_more = total - amount
            print(f'You need to pay more {need_more}')
        else:
            back = amount - total
            print(f'Thank you, here is your return money: {back}')
 
swapan = Shopping('Alen Swapan')
swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)

print(swapan.cart)
swapan.check_out(800)