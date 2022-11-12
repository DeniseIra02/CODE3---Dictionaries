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
input_of_user = input("What do you want to do? (Choose 1-3): ")

#codings 
if input_of_user == 1:
    user_fullName = input("Enter your Fullname. \n Full Name: ")
    user_gender = input("Enter your Gender. \n Gender: ")
    user_age = input("Enter your Age. \n Age:")
    user_bdate = input("Enter your birthdate. \n Birthdate: ")
    user_add = input("Enter your Address. \n Address: ")
    user_phoneNumber = input("Enter your Phone Number. \n Phone Number: ")
    user_vacc = input("Enter what is your Vaccine . \n Vaccine: ")
    user_vaccstat = input("Enter what is your Vaccine Status. \n Vaccine Status: ")
    
    print("Saved!")
    
    