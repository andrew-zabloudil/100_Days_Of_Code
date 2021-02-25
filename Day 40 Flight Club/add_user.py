from data_manager import DataManager

data_manager = DataManager()

print("Welcome to the Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_verification = input("Type your email again.\n")

if email == email_verification:
    print("You're in the club!")
    data_manager.add_user(first_name, last_name, email)
else:
    print("The email addresses did not match. Please try again.")
