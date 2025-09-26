# print all the words starting with s
st = 'Sam print words with starting with s! its simple!'
for word in st.split():
    # if(word[0]) == 's':
    # if(word[0]) == 's' or (word[0]) == 'S':
    if(word[0]).lower() == 's':
        print(word)
print("\n")
#output:
# starting
# s!
# simple!

#using list
swords = [word for word in st.split() if word[0].lower() == 's' ]
print(swords)
print("\n")
#output: ['Sam', 'starting', 's!', 'simple!']

#print all even number from 0-10
for n in range(0,10):
    if(n%2) == 0:
        print(n)
print("\n")
#output: 
# 0
# 2
# 4
# 6
# 8

#use range to print all the even number fro 0-10
print(list(range(0,11,2)))
print("\n")
#output: [0, 2, 4, 6, 8, 10]
for num in range(0,11,2):
    print(num)
print("\n")
# 0
# 2
# 4
# 6
# 8
# 10

#use list comprehension to create list of all numbers divisible by 3 between 1-50
mylist = [num for num in range(0,20) if num%3 == 0]
print(mylist)
print("\n")
#output: [0, 3, 6, 9, 12, 15, 18]