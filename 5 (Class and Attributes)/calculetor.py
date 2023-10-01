class Calculation:
    brand = 'Casio MS900'
    
    # Sum
    def add(self, num1, num2):
        result = num1 + num2
        print(result)
    
    # Sum
    def deduct(self, num1, num2):
        result = num1 - num2
        print(result)

    # Multiply
    def multiply(self, num1, num2):
        result = num1 * num2
        print(result)

    # Divide
    def divide(self, num1, num2):
        result = num1 / num2
        print(result)



find_result = Calculation()
print(find_result.brand)
find_result.add(5,2)
find_result.deduct(5, 2)
find_result.multiply(5, 2)
find_result.divide(6, 2)