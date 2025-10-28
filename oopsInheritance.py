class Animal():
    
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am")

    def eat(self):
        print("I eat")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        # return super().who_am_i()
        print("I am a dog") # overide the super class method

myanimal = Animal() #output: Animal created
myanimal.eat() #output: I eat
myanimal.who_am_i() #output: I am

my_dog = Dog()
#output
# Animal created
# Dog created
my_dog.who_am_i()
