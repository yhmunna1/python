class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height= height
        self.weight = weight
    
    def eat(self):
        print('Bhat khaye')

    def excercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override:
    def eat(self):
        print('Vegetables')

    def excercise(self):
        print('Gym kori')

    
    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('Sakib', 35, 65, 72, 'BD')
# sakib.eat()
# sakib.excercise()

mushi = Cricketer('Mushi', 36, 52, 65, 'BD')

print(45 + 63)
print( 'Sakib' + 'Rakib')
print([12, 98] + [5,6,7,1,2])
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)
