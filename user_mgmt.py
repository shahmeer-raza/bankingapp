from dotenv import load_dotenv
from os import getenv
import mysql.connector

load_dotenv()

conn = mysql.connector.connect(
    host=getenv("DB_HOST"),
    user=getenv("DB_USER"),
    passwd=getenv("DB_PASSWORD"),
    database=getenv("DB_NAME"),
)


def add_user(name, password, available_id):
    cursor = conn.cursor()
    cursor.execute(
        "insert into users(account_id, account_name, account_balance, account_password) values (%s,%s, %s, %s)",
        (available_id, name, 0, password),
    )
    conn.commit()
    cursor.close()


def user_exists(entered_id):
    cursor = conn.cursor()
    cursor.execute(
        "select account_name from users where account_id = %s", (entered_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    if not result:
        return False
    return True


def get_user_password(entered_id):
    cursor = conn.cursor()
    cursor.execute(
        "select account_password from users where account_id = %s", (entered_id,)
    )
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def get_user_from_id(wanted_id):
    cursor = conn.cursor()
    cursor.execute("select account_name from users where account_id = %s", (wanted_id,))
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def get_user_balance(user_id):
    cursor = conn.cursor()
    cursor.execute(
        "select account_balance from users where account_id = %s", (user_id,)
    )
    result = cursor.fetchone()[0]
    cursor.close()
    return result


def transfer_balance(amount, recipient_id, sender_id):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "update users set account_balance=account_balance-%s where account_id=%s",
            (amount, sender_id),
        )
        cursor.execute(
            "update users set account_balance=account_balance+%s where account_id=%s",
            (amount, recipient_id),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        cursor.close()
        print(e)
        return False
    cursor.close()
    return True

def update_password(new_password, user_id):
    cursor = conn.cursor()
    cursor.execute('update users set account_password = %s where account_id = %s', (new_password, user_id))
    conn.commit()
    cursor.close()
