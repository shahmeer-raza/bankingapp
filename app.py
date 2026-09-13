from time import sleep
from dashboard import dashboard
from os import system
from login_page import login_page
from signup_page import sign_up

system("clear")
while True:
    system("clear")
    print("__Welcome to SR Bank__")
    print("1. Sign up\n2. Login\n3. Exit")
    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("Please Enter a valid input")
        sleep(1.5)
        continue

    if choice not in [1, 2, 3]:
        print("Please Enter a valid input")
        sleep(1.5)
        continue
    
    elif choice == 1:
        system('clear')
        acc_created, user_id = sign_up()
        if acc_created:
            system('clear')
            print("User Added Successfully!")
            print(f"Your account Id is: {user_id}")
            sleep(1.5)
            system('clear')
            dashboard(user_id)

        else:
            system('clear')
            print("Sign up failed!")
            sleep(1.5)

    elif choice == 2:
        system("clear")
        result, logged_in_id, minutes_remaining = login_page()
        if result is True:
            system("clear")
            print("Logged In!")
            sleep(1.5)
            system("clear")
            dashboard(logged_in_id)
        elif result == 'restricted':
            seconds_remaining = minutes_remaining*60
            minutes = int(seconds_remaining // 60)
            seconds = int(seconds_remaining % 60)
            print(f"Max login attempt reached, wait for {minutes}:{seconds} minutes to try again!")
            sleep(2)
        elif result is None:
            print("User does not exist!")
            sleep(1.5)
        else:
            print("Access Denied!")
            sleep(1.5)

    elif choice == 3:
        break
