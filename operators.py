for num in range(5):
    print(num)
print("\n")
#output:
# 0
# 1
# 2
# 3
# 4

for num in range(2, 5):
    print(num)
print("\n")
#output:
# 2
# 3
# 4

for num in range(0, 10, 2):
    print(num)
print("\n")
#output:
# 0
# 2
# 4
# 6
# 8

index_count = 0
for letter in 'abcde':
    print(f'at index {index_count} the letter is {letter}')
    index_count += 1
print("\n")
#output:
# at index 0 the letter is a
# at index 1 the letter is b
# at index 2 the letter is c
# at index 3 the letter is d
# at index 4 the letter is e

word = "abcde"
for letter in enumerate(word):
    print(letter)
print("\n")
#output:
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

for index,letter in enumerate(word):
    print(index)
    print(letter)
print("\n")
#output:
# 0
# a
# 1
# b
# 2
# c
# 3
# d
# 4
# e

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

zip (mylist1,mylist2)

for item in zip (mylist1,mylist2):
    print(item)
print("\n")
#output:
# (1, 'a')
# (2, 'b')
# (3, 'c')

# to check resukt if list are uneven
mylist3 = [10,20,30,40,50]
for item in zip (mylist1,mylist2,mylist3):
    print(item)
print("\n")
#output:
# (1, 'a', 10)
# (2, 'b', 20)
# (3, 'c', 30)

#we can combain different list by zip
print(list(zip(mylist2,mylist3)))
print("\n")
#output: [('a', 10), ('b', 20), ('c', 30)]

# 'in' operator
result = 'X' in [1,2,3]
print(result)
print("\n")
#output: False

result = 'X' in ['X','Y','Z']
print(result)
print("\n")
#output: True

result = 'A' in 'A world'
print(result)
print("\n")
#output: True

# 'in' with dictionary
d = {'mykey':111, 'mykey1':222}
result = 'mykey' in d
print(result)
print("\n")
#output: True

result = 'mykey' in d.keys()
print(result)
print("\n")
#output: True

result = 222 in d.values()
print(result)
print("\n")
#output: True

# min, max, sum
mylist4 = [100,200,300,400,500]
print(min(mylist4)) #output:  100
print(max(mylist4)) #output:  500
print(sum(mylist4)) #output: 1500


# we can import many other functions from random
from random import shuffle
mylist4 = [100,200,300,400,500]
result = shuffle(mylist4)
print(mylist4)
#output: [400, 500, 100, 300, 200]

print(type(result)) # it has no data type
#output : <class 'NoneType'>

from random import randint
#to get random number between 0-50
print(randint(0,50))
#output: 23 

# input operator
name = input('what is your name?') #give input anjana
# note: input always accepts string as input
print(f'Welcome {name}!')
num = input('favorite number?')
print(f'fav num {num}, type ', type(num))
print(int(num)) #converting num to int
#output: 
# what is your name?anjana
# Welcome anjana!
# favorite number?51
# fav num 51, type  <class 'str'>
# 51



