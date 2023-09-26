# Global Vs Local variable (We need to use 'global' to modify global variable from local variable)

balance =500

def buy(price):
    global balance
    balance = balance - price
    print('Balance after buying:', balance)

buy(300)