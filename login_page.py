from user_mgmt import (
    user_exists,
    get_user_password,
    get_last_restricted_time,
    restrict_user,
)
import bcrypt
from datetime import datetime


def login_page():
    print("--login page--")
    entered_id = input("Enter your account_id: ").strip()
    if user_exists(entered_id):
        last_restricted_time = get_last_restricted_time(entered_id)
        if last_restricted_time:
            minutes_passed = (
                datetime.now() - last_restricted_time
            ).total_seconds() / 60
            minutes_remaining = 5 - minutes_passed
            if minutes_remaining > 0:
                return "restricted", None, minutes_remaining
        stored_password = get_user_password(entered_id)
        for i in range(3):
            entered_password = input("Enter your password: ").strip()
            if bcrypt.checkpw(
                entered_password.encode("utf-8"), stored_password.encode("utf-8")
            ):
                return True, entered_id, None
            elif i < 2:
                print("Wrong password, Try again!")
                continue
        restrict_user(entered_id)
        return False, None, None
    else:
        return None, None, None

