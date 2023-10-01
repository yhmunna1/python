class Shop:

    cart=[]
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehu = Shop('Mehu')
mehu.add_to_cart('Shoes')
mehu.add_to_cart('Phone')
print(mehu.cart)


nisho = Shop('Nisho')
nisho.add_to_cart('Cap')
nisho.add_to_cart('Tshirt')
print(nisho.cart)