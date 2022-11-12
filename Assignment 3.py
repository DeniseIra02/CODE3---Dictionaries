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

#Ask user what to do
input_of_user = int(input("What do you want to do? (Choose 1-3): "))
print("*****************************")
print()

#codings 
if input_of_user == 1:
    user_fullName = input("Enter your Fullname. \n Full Name: ")
    print()
    user_gender = input("Enter your Gender. \n Gender: ") 
    print()
    user_age = int(input("Enter your Age. \n Age:"))
    print()
    user_bdate = input("Enter your birthdate. \n Birthdate: ")
    print()
    user_add = input("Enter your Address. \n Address: ")
    print()
    user_phoneNumber = int(input("Enter your Phone Number. \n Phone Number: "))
    print()
    user_vacc = input("Enter what is your Vaccine. \n Vaccine: ")
    print()
    user_vaccstat = input("Enter what is your Vaccine Status. \n Vaccine Status: ")
    print()
    print("Saved!")
    print()
    print("*****************************")

#Declaring dictionary
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
