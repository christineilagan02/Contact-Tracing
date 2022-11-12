dict_info = {
    "Jiya Fuentes" : ['19', 'Male', 'Antipolo', 'jiya17@gmail.com', '0912372672541'],
    "Jelenie Wilson" : ["21", "Female", "Bulacan", "jelenzie90@gmail.com", "09925382417"],
    "Tininin Stanford" : ["18", "Female", "Mindoro", "tin02@gmail.com", "096782419017"]
}
print("\t\33[1m     Please enter the name \n     to display the record.\33[0m")
print()
user_want = input("\t\33[1m>> \33[0m").title()
print()
print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
print()
input_name = dict_info.get(user_want)
print("Fullname:", user_want)
print("\t\33[1mThis is", user_want, "record.\n\33[0m")
print("Fullname:", user_want)
for info in input_name, dict_info:
    print("Age:", info[0])
    print("Gender:", info[1])
    print("Address:", info[2])
    print("Email:", info[3])
    print("Phone Number:", info[4])