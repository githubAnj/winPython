myList = [1,2,3,4,5]

#to iterate through myList
for num in myList: # num is variable name for elements in mylist. choose any name
    print(num)
print("\n") 
#output:
# 1
# 2
# 3
# 4
# 5

#to iterate through myList
for jelly in myList:
    print("Hello!")
print("\n")
#output:
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!

#Print only even numbers in list
for num in myList:
    #check for even numner
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number:{num}')
print("\n")
#output:
# Odd number:1
# 2
# Odd number:3
# 4
# Odd number:5

#To get sum of every number in list
list_sum = 0
for num in myList:
    list_sum += num
print(list_sum)
print("\n")
#output: 15

#to iterate through the string
myString = "Hello!"
for letter in myString:
    print(letter)
print("\n")
#output:
# H
# e
# l
# l
# o
# !

#when you dont want to use any variable name
for _ in myString:
    print('Cool!')
print("\n")
#output:
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!

#to iterate through tuple
tup = (1,2,3)
for item in tup:
    print(item)
print("\n")
#output:
# 1
# 2
# 3

#to iterate through list which has tuples
myList = [(1,2),(3,4),(5,6)] # a list which has items as tuples pairs in the list
# print(len(myList)) #output: 3
for item in myList:
    print(item)
print("\n")
#output:
# (1, 2)
# (3, 4)
# (5, 6)

#to iterate through list which has tuples, and tuple unpacking
for a,b in myList: # both are same 'for (a,b) in myList:'
    print(a)
    print(b)
print("\n")
#output:
# 1
# 2
# 3
# 4
# 5
# 6

for a,b in myList: # both are same 'for (a,b) in myList:'
    print(b)
print("\n")
#output:
# 2
# 4
# 6

myList2 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myList2:
    print(b)
print("\n")
#output:
# 2
# 5
# 8

#to iterate through dictionary
d2 = {'k1':1,'k2':2,'k3':3}
for item in d2:
    print(item) #by defalt dictionaries only iterate through key
print("\n")
#output:
# k1
# k2
# k3

#to iterate through dictionary items
for item in d2.items(): # .items() to get item values
    print(item) #by defalt dictionaries only iterate through key
print("\n")
#output:
# ('k1', 1)
# ('k2', 2)
# ('k3', 3)

#to iterate through dictionary items with key and values
for key,value in d2.items(): # 
    print(key) 
    print(value) 
print("\n")
#output:
# k1
# 1
# k2
# 2
# k3
# 3

#to iterate through dictionary items get only values
for value in d2.values(): # 
    print(value) 
print("\n")
#output:
# 1
# 2
# 3