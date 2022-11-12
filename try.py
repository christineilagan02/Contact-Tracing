user_cpnumber = int(input("Phone Number: "))
if len(user_cpnumber) < 11:
    print("Your phone number must be 11 digits.")
    user_cpnumber = input("Phone Number: ")
    if len(user_cpnumber) > 11:
        print("Your phone number must be 11 digits.")
        user_cpnumber = input("Phone Number: ")