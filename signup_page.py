import bcrypt
from random import randint
from user_mgmt import add_user, user_exists

def sign_up():
    print("--Sign up page--")
    
    # getting name from user
    while True:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            print("this field can not be empty!")
            continue
        break

    # getting password from user
    while True:
        user_password = input("Set your password: ").strip()
        if not user_password:
            print("this field can not be empty!")
            continue
        if len(user_password) < 8:
            print("password must be 8 characters long!")
            continue
        break


    # confirming password from user
    for i in range(3):
        confirm_pass = input("Enter your password again to confirm: ").strip()
        if user_password == confirm_pass:
            break
        if i < 2:
            print("Wrong password try again!")
    else:
        print("Password confirmation failed!")
        return False

    # hashing the password
    hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # generating account id for user
    while True:
        user_id = str(randint(1000000000000000, 9999999999999999))
        if not user_exists(user_id):
            break

    add_user(user_name, hashed_password, user_id)
    return True, user_id
