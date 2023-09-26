
""" 
def full_name(first, last):
    name = f'Full Name: {first} {last}'
    return name

# name = full_name('Yeasin', 'Munna')
name = full_name(last='Munna', first='Yeasin')
print(name)
 """

def famous_name(firstName, lastName, **kargs):
    name= f'{firstName} {lastName}'
    # print(addition['title'])
    for key, value in kargs.items():
        print(key, value)
    return name

name = famous_name(firstName='Yeasin', lastName='Munna', middleName='Hossen', shortForm='YH', fullShort='YHM')
print(name)


# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    multi = num1 * num2
    remain = num1 - num2
    # return [sum, multi, remain]
    return sum, multi, remain


everything = a_lot(55, 21)
print(everything)