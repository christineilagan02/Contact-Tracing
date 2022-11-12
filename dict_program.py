# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# What do you want to do? (1-3): 3
# Exit? n

#--------------------------------
# Dictionary
dict_info = {

}

# Display a menu of options
print()
print("\t\33[1m\33[33m*\33[0m---+---+---+--\33[1m\33[33mMENU\33[0m--+---+---+---\33[1m\33[33m*\33[0m")
print()
menu_list = ["\t\33[3m\33[1m     1 => Append a new item \33[0m", 
             "\t\33[3m\33[1m     2 => Search an item \33[0m", 
             "\t\33[3m\33[1m     3 => Exit (y/n) \33[0m"]
for item in menu_list:
    print(item)


while True:
    print()
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    print()
    user_choice = int(input("\t  Which option do you prefer? "))    
    print()
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    print()
    # Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
    if user_choice == 1:
        print("\tPlease fill out the following details.")
        user_name = input("\tFull Name: ").title()
        user_age = int(input("\tAge: "))
        
        user_gender = str(input("\tGender (Male/Female): ")).title()
        valid_gender = ["Male", "Female"]
        while user_gender not in valid_gender:
            print("\tOnly type Male and Female")
            user_gender = input("\tGender: ")

        user_address = input("\tAddress: ").title()
        user_email = input("\tEmail: ")
        while "@" not in user_email:
            print("\tYour email address must have '@' in it.")
            user_email = input("\tEmail: ")
            if ".com" not in user_email:
                print("\tYour email address must have '.com' in it.")
                user_email = input("\tEmail: ")
        while ".com" not in user_email:
            print("\tYour email address must have '.com' in it.")
            user_email = input("\tEmail: ")
            if "@" not in user_email:
                print("\tYour email address must have '@' in it.")
                user_email = input("\tEmail: ")
        user_cpnumber = input("\tPhone Number: ")
        if len(user_cpnumber) < 11:
            print("\tYour phone number must be 11 digits.")
            user_cpnumber = input("\tPhone Number: ")
            if len(user_cpnumber) > 11:
                print("\tYour phone number must be 11 digits.")
                user_cpnumber = input("\tPhone Number: ")
        
        print()
        print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
        print()
        
        # Storing info
        dict_info[user_name] = [user_age, user_gender, user_address, user_email, user_cpnumber]
        print("\t\33[1m\33[93m\33[3m   Info Saved!\33[0m")
        
    # Option 2: Search, ask full name then display the record
    elif user_choice == 2:
        print("\t     Please enter the name \n     to display the record.")
        print()
        user_want = input("\t>> ").title()
        print()
        print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
        print()
        input_name = dict_info.get(user_want)
        print("\tThis is", user_want, "record.\n")
        for info in input_name:
            print("\t", info)
        

    # Option 3: Ask the user if want to exit or retry.

    elif user_choice == 3:
        exit = input("\tAre you sure?(y/n) ").title()
        
        if exit == "Y":
            import sys 
            print()
            print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
            print()
            print ("\t\33[1m\33[93m\33[3m        You can now exit.\33[0m")
            print()
            print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
            print()
            sys.exit("\n")