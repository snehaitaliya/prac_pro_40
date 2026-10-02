#A Bank Management System is a software application used to manage customer accounts and banking transactions. It allows users to create accounts, deposit and withdraw money, transfer funds, and check account balances securely.

f=open("bank.txt","a")

while True:
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Funds")
    print("5. Check Balance")
    print("6. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        account_number=input("Enter Account Number: ")
        name=input("Enter Name: ")
        balance=float(input("Enter Initial Balance: "))
        f.write(f"{account_number}\t{name}\t{balance}\n")
        print("Account created successfully!")

    elif choice==2:
        account_number=input("Enter Account Number: ")
        amount=float(input("Enter Amount to Deposit: "))
        f=open("bank.txt","r")
        data=f.readlines()
        f.close()
        f=open("bank.txt","w")
        for line in data:
            acc_num, name, bal=line.strip().split("\t")
            if acc_num==account_number:
                bal=float(bal)+amount
                print(f"Deposited {amount}. New Balance: {bal}")
            f.write(f"{acc_num}\t{name}\t{bal}\n")
        f.close()

    elif choice==3:
        account_number=input("Enter Account Number: ")
        amount=float(input("Enter Amount to Withdraw: "))
        f=open("bank.txt","r")
        data=f.readlines()
        f.close()
        f=open("bank.txt","w")
        for line in data:
            acc_num, name, bal=line.strip().split("\t")
            if acc_num==account_number:
                bal=float(bal)
                if bal>=amount:
                    bal-=amount
                    print(f"Withdrew {amount}. New Balance: {bal}")
                else:
                    print("Insufficient balance!")
            f.write(f"{acc_num}\t{name}\t{bal}\n")
        f.close()

    elif choice==4:
        from_account=input("Enter Your Account Number: ")
        to_account=input("Enter Recipient's Account Number: ")
        amount=float(input("Enter Amount to Transfer: "))

        f=open("bank.txt","r")
        data=f.readlines()
        f.close()

        from_account_found=False
        to_account_found=False
        from_balance=0
        to_balance=0

        for line in data:
            acc_num, name, bal=line.strip().split("\t")
            if acc_num==from_account:
                from_account_found=True
                from_balance=float(bal)
            elif acc_num==to_account:
                to_account_found=True
                to_balance=float(bal)

        if not from_account_found:
            print("From account not found!")
        elif not to_account_found:
            print("To account not found!")
        elif from_balance < amount:
            print("Insufficient balance in from account!")
        else:
            from_balance -= amount
            to_balance += amount

            f=open("bank.txt","w")
            for line in data:
                acc_num, name, bal=line.strip().split("\t")
                if acc_num==from_account:
                    f.write(f"{acc_num}\t{name}\t{from_balance}\n")
                elif acc_num==to_account:
                    f.write(f"{acc_num}\t{name}\t{to_balance}\n")
                else:
                    f.write(line)
            f.close()
            print(f"Transferred {amount}. New Balance in From Account: {from_balance}, New Balance in To Account: {to_balance}")

    elif choice==5:
        account_number=input("Enter Account Number: ")
        f=open("bank.txt","r")
        data=f.readlines()
        f.close()
        found=False
        for line in data:
            acc_num, name, bal=line.strip().split("\t")
            if acc_num==account_number:
                found=True
                print(f"Account Number: {acc_num}, Name: {name}, Balance: {bal}")
                break
        if not found:
            print("Account not found!")

    elif choice==6:
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

f.close()