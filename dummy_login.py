import getpass # to hide password input

#fixed USERNAME and PASSWORD
USERNAME = "admin"
PASSWORD = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user = input("enter user name: ")
    # pwd = input("Enter password: ")
    pwd = getpass.getpass("Enter password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login successfull!", user)
        #break

        #show menu
        # while true:
        #     print("---- MENU ----")
        #     print("1. Calulation")
        #     print("2. Vote Eligiblity")
        #     print("3. EXit")

        #     choice = input("Enter your choice")

    else:
        attempts+= 1
        print("invalid login credentials. Attempts left : ", max_attempts - attempts)


    

if attempts == max_attempts:
    print("Account locked, Too many failed attempts")