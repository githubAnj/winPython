myList = [1,2,3,4,5]

#to iterate throgh myList
for num in myList: # num is variable name for elements in mylist. choose any name
    print(num) 
#output:
# 1
# 2
# 3
# 4
# 5

#to iterate throgh myList
for jelly in myList:
    print("Hello!")
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
#output: 15

#to iterate throgh the string
myString = "Hello!"
for letter in myString:
    print(letter)
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
#output:
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!

#to iterate throgh tuple
tup = (1,2,3)
for item in tup:
    print(item)
#output:
# 1
# 2
# 3

#to iterate throgh list which has tuples
myList = [(1,2),(3,4),(5,6)] # a list which has items as tuples pairs in the list
# print(len(myList)) #output: 3
for item in myList:
    print(item)
#output:
# (1, 2)
# (3, 4)
# (5, 6)

#to iterate throgh list which has tuples, and tuple unpacking
for a,b in myList: # both are same 'for (a,b) in myList:'
    print(a)
    print(b)
#output:
# 1
# 2
# 3
# 4
# 5
# 6

for a,b in myList: # both are same 'for (a,b) in myList:'
    print(b)
#output:
# 2
# 4
# 6

myList2 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myList2:
    print(b)
#output:
2
5
8