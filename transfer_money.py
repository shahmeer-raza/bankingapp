from os import system
from user_mgmt import get_user_balance, user_exists, transfer_balance


def transfer_money(user_id):
    recipient_id = input("Enter recipient account ID: ")
    if not user_exists(recipient_id):
        print("User does not exist!")
        return False
    try:
        amount = int(input("Enter amount to transfer: "))
    except ValueError:
        print("Please Enter a valid input!")
        return False
    user_balance = get_user_balance(user_id)
    if recipient_id == user_id:
        print("This action can not be performed!")
        return False
    elif amount <=0:
        print("This action can not be performed!")
        return False
    elif user_balance< amount:
        print("Insufficient balance!")
        return False
    else:
        return transfer_balance(amount, recipient_id, user_id)
    


# transfer_money(7807016038733695)
