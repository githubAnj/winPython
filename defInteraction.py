from random import shuffle

def shuffel_list(mylist):
    shuffle(mylist)
    return mylist
 
def player_game():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("pick a number 0,1, or 2 ") #input will be in string
        
    return int(guess) #convert input to int

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('correct!')
    else:
        print("worng guess!")
        print(mylist)

#initial list
mylist = [' ', '0', ' ']
#shuffle list
mixed_list = shuffel_list(mylist)
print(mixed_list)
#user guess
guess = player_game()
#check user guess
myindex = check_guess(mixed_list,guess)

