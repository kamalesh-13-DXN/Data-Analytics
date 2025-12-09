name = ["Alice", "Bob", "Charlie", "David", "Emma", "Francis", "Gokul", "Hariharan", "Raja", "Karthick"]
reg_no = [1501,1502,1503,1504,1505,1506,1507,1508,1509,1510]
password = [111,112,113,114,115,116,117,118,119,120]
print("\n----- LOGIN / REGISTRATION PORTAL -----")
rno = int(input("Enter your register number: "))
if rno in reg_no:
    i = reg_no.index(rno)
    psw = int(input("Enter your password: "))
    if psw == password[i]:
        print("WELCOME", name[i])
    else:
        print("INCORRECT PASSWORD")
else:
    print("INVALID USER ID")
    a = int(input("TO CREATE A NEW ACCOUNT PRESS 1: "))
    if a == 1:
        n = input("ENTER YOUR NAME: ")
        r = int(input("CREATE YOUR REGISTER NUMBER: "))
        p = int(input("CREATE YOUR PASSWORD: "))
        name.append(n)
        reg_no.append(r)
        password.append(p)
        print("ACCOUNT CREATED SUCCESSFULLY!")
        rno2 = int(input("\nENTER YOUR REGISTER NUMBER: "))
        if rno2 in reg_no:
            j = reg_no.index(rno2)
            psw2 = int(input("ENTER YOUR PASSWORD: "))
            if psw2 == password[j]:
                print("WELCOME", name[j])
            else:
                print("INCORRECT PASSWORD")
        else:
            print("INVALID USER ID")
    else:
        print("EXIT")
