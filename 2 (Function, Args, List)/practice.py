def sum_all(*args):
    sum=0
    for  arg in args:
        sum = sum +arg
    return sum

result = sum_all(10, 5, 10, 5, 50, 20)
print(result)