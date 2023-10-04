from abc import ABC, abstractmethod
# abc = abstract base class

class Animal(ABC):
    @abstractmethod #Enforce all derived class to have a (eat) method
    def eat(self):
        print('I Need Food')
    @abstractmethod #Enforce all derived class to have a (move) method
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('hey nananana!, eating banana')

    def move(self):
        pass

layka = Monkey('lucky')
layka.eat()