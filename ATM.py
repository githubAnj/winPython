balance = 10000

while True:
    print("---menu---")
    print("1. check balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Current Balance:", balance)
    
    elif choice == "2":
        amount = float(input("Enter amount to deposite: "))
        balance += amount
        print(f"Deposited {amount}.  New Balance: {balance}")
    
    elif choice == "3":
        amount = float(input("enter the amout to withdarw"))
        # withdrawAmount = balance - amount
        # if withdrawAmount < 0:
        #     print("you dont have sufficent balance")
        #     break
        # else: 
        #     balance -= amount
        #     print(f"your current balance is {balance}")
        if amount <= balance:
            balance -= amount
            print(f"✅ Withdrawn {amount}. New Balance: {balance}")
        else:
            print("❌ Insufficient funds!")
    elif choice == 4:
        print("👋 Thank you for using ATM!")
        break
          



