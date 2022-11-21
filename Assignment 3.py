from colorama import Fore, Back, Style

#Menu
print()
print(Fore.CYAN + "*****************************")
print()
print(Fore.WHITE + "Hello User! Let's Save your Contact Information.")
print()
print(Fore.CYAN + "*****************************")
print()
print(Fore.MAGENTA + "************MENU*************")
print()
print(Fore.MAGENTA + "     1 -> Add an item")
print(Fore.MAGENTA + "     2 -> Search")
print(Fore.MAGENTA + "     3 -> Exit")
print()
print(Fore.CYAN + "*****************************")
print()

all_info = {}

while True:
    #Ask user what to do
    input_of_user = int(input(Fore.WHITE + "What do you want to do? (Choose 1-3): "))
    print()
    print(Fore.CYAN + "*****************************")
    print()

    #codings for option 1
    if input_of_user == 1:
        user_fullName = input(Fore.WHITE + "Enter your Fullname. \n Full Name: ")
        print()
        user_gender = input(Fore.WHITE + "Enter your Gender. \n Gender: ") 
        print()
        user_age = input(Fore.WHITE + "Enter your Age. \n Age: ")
        print()
        user_bdate = input(Fore.WHITE + "Enter your birthdate. \n Birthdate: ")
        print()
        user_add = input(Fore.WHITE + "Enter your Address. \n Address: ")
        print()
        user_phoneNumber = input(Fore.WHITE + "Enter your Phone Number. \n Phone Number: ")
        print()
        user_vacc = input(Fore.WHITE + "Enter what is your Vaccine. \n Vaccine: ")
        print()
        user_vaccstat = input(Fore.WHITE + "Enter what is your Vaccine Status. \n Vaccine Status: ")
        print()
        print(Fore.GREEN + "Saved!")
        print()
        print(Fore.CYAN + "*****************************")
        
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
        
        all_info[user_fullName] = user_info
        
        print()
        print(Fore.MAGENTA + "************MENU*************")
        print()
        print(Fore.MAGENTA + "     1 -> Add an item")
        print(Fore.MAGENTA + "     2 -> Search")
        print(Fore.MAGENTA + "     3 -> Exit")
        print()
        print(Fore.CYAN + "*****************************")
        print()
        input_of_user = int(input(Fore.WHITE + "What do you want to do? (Choose 1-3): "))
        print()
        print(Fore.CYAN + "*****************************")
        print()
        
        #codings for option 2
        if input_of_user == 2: 
            user_fullName2 = input(Fore.WHITE + "Enter your Fullname. \n Full Name: ")
            print()
            if user_fullName2 in all_info:
                print(Fore.BLUE + "**********USER INFO**********")
                print()
                search_data = all_info[user_fullName2]
                for  key, value in search_data.items():   
                    print(Fore.BLUE + key, ":", value)
            else:
                print(Fore.CYAN + "*****************************")
                print("!Invalid User Name!")
            
            print()   
            print(Fore.CYAN + "*****************************")
            print()
            print(Fore.MAGENTA + "************MENU*************")
            print()
            print(Fore.MAGENTA + "     1 -> Add an item")
            print(Fore.MAGENTA + "     2 -> Search")
            print(Fore.MAGENTA + "     3 -> Exit")
            print()
            print(Fore.CYAN + "*****************************")
            print()
            input_of_user = int(input(Fore.WHITE + "What do you want to do? (Choose 1-3): "))
            print()
            print(Fore.CYAN + "*****************************")
            print()
                
        #codings for option 3
        if input_of_user == 3:
            user_yes_no = input(Fore.WHITE + "Do you want to Exit? (Yes/No): ")
            if user_yes_no == "Yes":
                break
            else:
                print(Fore.CYAN + "*****************************")
                print()
                print(Fore.MAGENTA + "************MENU*************")
                print()
                print(Fore.MAGENTA + "     1 -> Add an item")
                print(Fore.MAGENTA + "     2 -> Search")
                print(Fore.MAGENTA + "     3 -> Exit")
                print()
                print(Fore.CYAN + "*****************************")
                print()