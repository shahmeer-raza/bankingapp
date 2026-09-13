from os import system
from time import sleep
from user_mgmt import update_password
import bcrypt


def get_new_password(user_old_password):
    system("clear")
    for i in range(3):
        user_entered_password = input("Enter your current password: ")
        if bcrypt.checkpw(user_entered_password.encode('utf-8'), user_old_password.encode('utf-8')):
            break
        elif i < 2:
            print("Wrong Password, Try again!")
            continue
    else:
        return None

    while True:
        # getting new password from user
        system("clear")
        new_pass = input("Enter your new password: ")
        if not new_pass:
            print("This field cannot be empty!")
            sleep(1.5)
            continue
        elif len(new_pass) < 8:
            print("password must be 8 character long!")
            sleep(1.5)
            continue
        elif bcrypt.checkpw(new_pass.encode('utf-8'), user_old_password.encode('utf-8')):
            print("Your old password cannot be your new password!")
            sleep(1.5)
            continue

        # confirming password from user
        for i in range(3):
            confirmed_password = input("Enter your password again to confirm: ")
            if confirmed_password == new_pass:
                return bcrypt.hashpw(
                    new_pass.encode('utf-8'), bcrypt.gensalt()
                ).decode('utf-8')
            elif i < 2:
                print("Password did not match! Try again")
        return None


def settings_menu(user_id, user_old_password):
    while True:
        system("clear")
        print("--Settings--")
        print("\n1. Change password\n2. Exit")
        try:
            choice = int(input("\nEnter your choice (1/2): "))
        except ValueError:
            print("Please Enter a valid input!")
            continue

        if choice not in [1, 2]:
            print("Please Enter a valid input!")
            continue

        elif choice == 1:
            new_password = get_new_password(user_old_password)
            if new_password is None:
                print("Request Failed!")
                sleep(1.5)
            else:
                update_password(new_password, user_id)
                system("clear")
                print("Password updated successfully!")
                sleep(1.5)
                system("clear")

        elif choice == 2:
            break
