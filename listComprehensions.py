# List Comprehensions are unique way creating list quickly
# If you are using for loop with .append() to create list the list comprehrnsion are useful

mystring = "Hello!"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
print("\n")
#output: ['H', 'e', 'l', 'l', 'o', '!']

# we can rewrite the above code in short with list comprehension
mylist = [letter for letter in mylist]
print(mylist)
print("\n")
#output: ['H', 'e', 'l', 'l', 'o', '!']

mylist = [x for x in 'world']
print(mylist)
print("\n")
#output: ['w', 'o', 'r', 'l', 'd']

mylist = [x for x in range(4,8)]
print(mylist)
print("\n")
#output: [4, 5, 6, 7]

mylist = [n*2 for n in range(0,3)] #to get the multiplication of number
print(mylist)
print("\n")
#output: [0, 2, 4]

mylist = [n**2 for n in range(0,3)] #to get the suare of number
print(mylist)
print("\n")
#output: [0, 1, 4]

mylist = [x for x in range(4,16,2)] # start: stop: jump: 
print(mylist)
print("\n")
#output: [4, 6, 8, 10, 12, 14]

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)
print("\n")
#output : [32.0, 50.0, 68.0, 94.1]

# if condition
mylist = [x**2 for x in range(0,15) if x%2 == 0]
print(mylist)
print("\n")
#output: [0, 4, 16, 36, 64, 100, 144, 196]

# if else condition
result = [x if x%2 == 0 else 'odd' for x in range(0,10)]
print(result)
print("\n")
# output: [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']

#nested loop
mylist = []
for x in [2,3,4]:
    for y in [1,2,3]:
        mylist.append(x*y)
print(mylist)
print("\n")
#output: [2, 4, 6, 3, 6, 9, 4, 8, 12]
    
#we can rewrite the above nested for as below with list comprehension
mylist = [x*y for x in [2,3,4] for y in [1,2,3]]
print(mylist)
print("\n")
#output: [2, 4, 6, 3, 6, 9, 4, 8, 12]