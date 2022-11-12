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
    "Jiya Fuentes" : ['19', 'Male', 'Antipolo', 'jiya17@gmail.com', '0912372672541'],
    "Jelenie Wilson" : ["21", "Female", "Bulacan", "jelenzie90@gmail.com", "09925382417"],
    "Tininin Stanford" : ["18", "Female", "Mindoro", "tin02@gmail.com", "096782419017"]
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
    user_choice = int(input("\t\33[1m  Which option do you prefer? "))    
    print()
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    print()
    # Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
    if user_choice == 1:
        print("\t\33[1mPlease fill out the following details.\33[0m")
        user_name = input("\t\33[1mFull Name: \33[0m").title()
        user_age = int(input("\t\33[1mAge: \33[0m"))
        
        user_gender = str(input("\t\33[1mGender (Male/Female): \33[0m")).title()
        valid_gender = ["Male", "Female"]
        while user_gender not in valid_gender:
            print("\t\33[1mOnly type Male and Female\33[0m")
            user_gender = input("\t\33[1mGender: \33[0m")

        user_address = input("\t\33[1mAddress: \33[0m").title()
        user_email = input("\t\33[1mEmail: \33[0m")
        while "@" not in user_email:
            print("\t\33[1mYour email address must have '@' in it.\33[0m")
            user_email = input("\t\33[1mEmail: \33[0m")
            if ".com" not in user_email:
                print("\t\33[1mYour email address must have '.com' in it.\33[0m")
                user_email = input("\t\33[1mEmail: \33[0m")
        while ".com" not in user_email:
            print("\t\33[1mYour email address must have '.com' in it.\33[0m")
            user_email = input("\t\33[1mEmail: \33[0m")
            if "@" not in user_email:
                print("\t\33[1mYour email address must have '@' in it.\33[0m")
                user_email = input("\t\33[1mEmail: \33[0m")
        user_cpnumber = input("\t\33[1mPhone Number: \33[0m")
        if len(user_cpnumber) < 11:
            print("\t\33[1mYour phone number must be 11 digits.\33[0m")
            user_cpnumber = input("\t\33[1mPhone Number: \33[0m")
            if len(user_cpnumber) > 11:
                print("\t\33[1mYour phone number must be 11 digits.\33[0m")
                user_cpnumber = input("\t\33[1mPhone Number: \33[0m")
        
        print()
        print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
        print()
        
        # Storing info
        dict_info[user_name] = [user_age, user_gender, user_address, user_email, user_cpnumber]
        print("\t\t\33[1m\33[93m\33[3m   Info Saved!\33[0m")
        
    # Option 2: Search, ask full name then display the record
    elif user_choice == 2:
        print("\t\33[1m     Please enter the name \n\t     to display the record.\33[0m")
        print()
        user_want = input("\t\33[1m>> \33[0m").title()
        print()
        print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
        print()
        input_name = dict_info.get(user_want)
        print("Fullname:", user_want)
        for info in input_name, dict_info:
            print(str("\t\33[33mAge: \33[0m") + info[0])
            print(str("\t\33[33mGender: \33[0m") + info[1])
            print(str("\t\33[33mAddress: \33[0m") + info[2])
            print(str("\t\33[33mEmail: \33[0m") + info[3])
            print(str("\t\33[33mPhone Number: \33[0m") + info[4])
            break

    # Option 3: Ask the user if want to exit or retry.

    elif user_choice == 3:
        exit = input("\t\33[1mAre you sure?(y/n) \33[0m").title()
        
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