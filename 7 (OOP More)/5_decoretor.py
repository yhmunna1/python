import math
import time
def timer(func):
    def inner(*args, **kwargs):
        print('Inner print')
        start = time.time()
        # print(func)
        end = time.time()
        func(*args, **kwargs)
        print(f'Total time taken: {end-start}')
    return inner

# timer()()

# @timer #This is decorator, Its a nested function
# def get_factorial():
#      print('get fun')
# get_factorial()

@timer
def get_factorial(n):
     print('get fun')
     result = math.factorial(n)
     print(f'Factorial of {n} is: {result}')

get_factorial(5)
get_factorial(n=7)