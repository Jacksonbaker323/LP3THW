## Animal is-a object
class Animal(object):
    def breathe(self):
        print("Whooosh")

# Dog is-a animal
class Dog(Animal):
    
    def __init__(self, name):
        #Dog has-a name
        self.name = name

    def bark(self):
        print("Woof!")

#Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a name
        self.name = name
    
    def meow(self):
        print("Meow!")

#Person is-a object
class Person(object):

    def __init__(self, name):
        #Person has-a name
        self.name = name

        #Person has-a pet
        self.pet = None

#Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        #Figure out what this does
        super(Employee, self).__init__(name)

        #Employee has-a salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    pass

#Salmon is-a fish
class Salmon(Fish):
    pass

#Halibut is-a fish
class Halibut(Fish):
    pass

#Rover is-a dog
rover = Dog("Rover")

#Satan is-a cat
satan = Cat("Satan")

#Mary is-a person
mary = Person("Mary")

#Mary has-a pet cat Satan
mary.pet = satan

#Frank is-a Employee and has-a salary of 120k
frank = Employee("Frank", 120000)

#Frank has-a pet dog Rover
frank.pet = rover

#Flipper is-a fish
flipper = Fish()

#Crouse is-a Salmon
crouse = Salmon()

#Harry is-a halibut
harry = Halibut()

rover.breathe()
rover.bark()
satan.breathe()
satan.meow()
