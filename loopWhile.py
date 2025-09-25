x = 0

while x < 5:
    print(f'the current value of x : {x}')
    x += 1
#output:
# the current value of x : 0
# the current value of x : 1
# the current value of x : 2
# the current value of x : 3
# the current value of x : 4

while x < 5:
    print(f'the current value of x : {x}')
    x += 1
else:
    print("x is not less then 5")

#output:
# x is not less then 


#pass, break , go key words

mystring = 'Sammy'

for letter in mystring:
    # print(letter)
    if letter == 'a':
        continue
    print(letter)
#output:
# s
# m
# m
# y
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
#output:
# 0
# 1