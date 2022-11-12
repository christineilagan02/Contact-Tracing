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
info = {
    "Jiya" : ["19", "Male", "Antipolo", "jiya17@gmail.com", "0912372672541"],
    "Jelenie" : ["21", "Female", "Bulacan", "jelenzie90@gmail.com", "09925382417"],
    "Tine" : ["18", "Female", "Mindoro", "tin02@gmail.com", "096782419017"]
}

# Display a menu of options
print()
print("*---+---+---+--MENU--+---+---+---*")
print()
menu_list = ["     1 -> Append a new item", 
             "     2 -> Search an item", 
             "     3 -> Exit (y/n)"]
for item in menu_list:
    print(item)
print()
print("*---+---+---+--MENU--+---+---+---*")
print()
user_choice = int(input("Which option do you prefer? "))    

# Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
if user_choice == 1:
    print("Please fill out the following details.")
    user_name = input("Name: ")
    user_age = int(input("Age: "))
    user_gender = input("Gender: ")
    user_address = input("Address: ")
    user_email = input("Email: ")
    user_cpnumber = int(input("Phone Number: "))
    
    info[user_name] = [user_age, user_gender, user_address, user_email, user_cpnumber]
    print("Saved!")
    

    # Use dictionary to store the info
    # Use the full name as key
    # The value is another dictionary of personal information
# Option 2: Search, ask full name then display the record
# Option 3: Ask the user if want to exit or retry.