class Shop:

    Shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #Cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mehu = Shop('Mehu')
mehu.add_to_cart('Shoes')
mehu.add_to_cart('Phone')
print('Mehu have: ', mehu.cart)


nisho = Shop('Nisho')
nisho.add_to_cart('Cap')
nisho.add_to_cart('Tshirt')
print('Nisho have: ', nisho.cart)


apurba = Shop('Apurba')
apurba.add_to_cart('Shirt')
apurba.add_to_cart('Sunglass')
print('Apurba have: ', apurba.cart)