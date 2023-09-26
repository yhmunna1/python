# deafult_args_kargs
""" 
def sum(num1, num2, num3= 0, num4=0):
    result = num1 +num2 +num3 +num4
    return result

total = sum(20, 30)
print('Total:',total)
 """

# Args: Sum infinity numbers
def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        sum = sum+num
    return sum

total = all_sum(45, 46, 47)
print('All Sum:', total)