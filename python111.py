msg = "hi Anjana"
print(msg.capitalize())

name = "Anjanaa"
age = 33
height = 5.4
is_dev = True
nothing = None

print(type(is_dev), type(name))

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

input_name = input("Enter your name: ")
print("Welcome",input_name)
input_age = int(input("Enter your age"))

if input_age >= 18:
    print("you can vote", input_name)
else:
    print("Wait for your turn")
