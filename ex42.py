## Animal is-a object (yes, sort of confusin) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal object
class Dog(Animal):

    def __init__(self, name):
        ## self has-a name attribute
        self.name = name

## Cat is-a Animal object
class Cat(Animal):

    def __init__(self, name):
        ## self has-a name attribute
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a name attribute
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person object
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## self has-a salary attribute
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a instance of the Cat class
satan = Cat("Satan")

## mary is-a instance of the Person class
mary = Person("Mary")

## mary has-a 'pet' attribute called satan
mary.pet = satan

## frank is-a Employee instance with the params name:"Frank" and salary:120000
frank = Employee("Frank", 120000)

## frank has-a pet attribute named rover
frank.pet = rover

## flipper is-a instance of class Fish
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is-a Halibut instance
harry = Halibut()
