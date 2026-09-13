from user_mgmt import user_exists, get_user_password
import bcrypt


def login_page():
    print("--login page--")
    entered_id = input("Enter your account_id: ").strip()
    if user_exists(entered_id):
        entered_password = input("Enter your password: ").strip()
        stored_password = get_user_password(entered_id)

        if bcrypt.checkpw(entered_password.encode('utf-8'), stored_password.encode('utf-8')):
            return True, entered_id
        return False, None
    else:
        return None, None
