name=input("Enter your name:")
age=int(input("Enter your age:"))
email=input("Enter your email:")
mobile_no=input("Enter your mobile n0:")
address=input("Enter your address:")
password=input("Enter minimum 6 character password:")
if age>=18:
    if len(password)>=6:
        print("\nRegistration is successful!!")
        print("----- DETAILS YOU GIVEN -----\n")
        print("Name:",name)
        print("Age:",age)
        print("Email:",email)
        print("Mobile No:",mobile_no)
        print("Address:",address)
    else:
        print("Password is too short and try it again")
else:
    print("age must be 18 or above to register")       
