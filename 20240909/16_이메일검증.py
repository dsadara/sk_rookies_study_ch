import re

def validate_email(email):
    # pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[.][a-zA-Z0-9.-]+$")
    pattern = re.compile(r"^[\w_.+-]+@[\w-]+[.][\w.-]+$")
    if pattern.match(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

user_email = input("Enter your email: ")
validate_email(user_email)