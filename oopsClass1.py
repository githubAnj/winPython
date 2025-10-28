
class Dog():
    #class attribute
    species = 'mammal'

    def __init__(self,breed,name):
        # we can take in the arguments
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name

    def bark(self):
        print("Woof! my name is {} " .format(self.name))

my_dog = Dog('lab','Nella')

my_dog.bark()



class Cirle():
    
    #attributes
    pi = 3.14

    def __init__(self, radius = 1): #radius default value 1
        
        self.radius = radius
        # self.area = radius*radius*self.pi #the below line also right
        self.area = radius*radius*Cirle.pi

    def get_circufrenace(self):
        return self.radius*self.pi*2
    
my_circle = Cirle(2)
print(my_circle.area)
print(my_circle.get_circufrenace())