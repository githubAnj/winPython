if True:
    print("Its true") #output: Its true

hungry = True

if hungry:
    print("Feed me!") #output: Feed me!

hungry = False
if hungry:
    print("Feed me!")
else:
    print("I am not hungry") 
#output: I am not hungry

loc = "Bank"
if loc == "Auto shop":
    print("Car is cool")
elif loc == "Bank":
    print("Money is cool")
elif loc == "shop":
    print("Welcome to the store")
else:
    print("I do not know much")
#output: Money is cool

name = "Sammy"
if name == "Frankie":
    print("Hey Frankie!")
elif name == "Sammy":
    print("Welcome Sammy")
else :
    print("I dont know!")
#output: Welcome Sammy