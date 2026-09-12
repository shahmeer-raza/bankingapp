from os import system
from random import choice
from time import sleep
from user_mgmt import get_user_from_id, get_user_balance
from transfer_money import transfer_money


def dashboard(loggedin_user_id):
    user_name = get_user_from_id(loggedin_user_id)
    while True:
        system("clear")
        print(f"--Welcome {user_name}--")
        print(f'--Account id: {loggedin_user_id}--')
        print("1. Check balance\n2. Transfer Money\n3. logout")
        try:
            choice = int(input("Enter your choice (1/2/3): "))
        except ValueError:
            system("clear")
            print("Please enter valid choice!")
            sleep(1.5)
            continue
        if choice not in [1, 2, 3]:
            system("clear")
            print("Please enter valid choice!")
            sleep(1.5)
            continue
        elif choice == 1:
            system("clear")
            user_balance = get_user_balance(loggedin_user_id)
            print(f"Your Account id: {loggedin_user_id}")
            print(f"Your Balance: {user_balance}$")
            input("Press Enter to exit!")
            continue
        elif choice == 2:
            system("clear")
            if transfer_money(loggedin_user_id):
                print("Transaction successfull!")
            else:
                print("Transaction Failed!")
            sleep(1.5)
            continue
        elif choice == 3:
            break
