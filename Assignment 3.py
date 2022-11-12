#Menu
print("*****************************")
print()
print("Hello User! Let's Save your Contact Information.")
print()
print("*****************************")
print()
print("************MENU*************")
print()
print("     1 -> Add an item")
print("     2 -> Search")
print("     3 -> Exit")
print()
print("*****************************")
print()

while True:
    #Ask user what to do
    input_of_user = int(input("What do you want to do? (Choose 1-3): "))
    print("*****************************")
    print()

    #codings for option 1
    if input_of_user == 1:
        user_fullName = input("Enter your Fullname. \n Full Name: ")
        print()
        user_gender = input("Enter your Gender. \n Gender: ") 
        print()
        user_age = input("Enter your Age. \n Age: ")
        print()
        user_bdate = input("Enter your birthdate. \n Birthdate: ")
        print()
        user_add = input("Enter your Address. \n Address: ")
        print()
        user_phoneNumber = input("Enter your Phone Number. \n Phone Number: ")
        print()
        user_vacc = input("Enter what is your Vaccine. \n Vaccine: ")
        print()
        user_vaccstat = input("Enter what is your Vaccine Status. \n Vaccine Status: ")
        print()
        print("Saved!")
        print()
        print("*****************************")
        
        #Declaring dictionaries
        user_info = {
            "Full Name": user_fullName,
            "Gender": user_gender,
            "Age": user_age,
            "Birthdate": user_bdate,
            "Address": user_add,
            "Phone Number": user_phoneNumber,
            "Vaccine": user_vacc,
            "Vaccine Status": user_vaccstat
        }
        
        input_of_user2 = int(input("What do you want to do? (Choose 1-3): "))
        print("*****************************")
        print()
        
        #codings for option 2
        if input_of_user2 == 2: 
            user_fullName2 = input("Enter your Fullname. \n Full Name: ")
            if user_fullName == user_fullName2:
                print()
                print("**********USER INFO**********")
                print()
                print(user_info)
                print("*****************************")
            else:
                print("*****************************")
                print("!Invalid User Name!")