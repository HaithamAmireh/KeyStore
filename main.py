import getpass
import os
import sqlite3
import sys
import time

from dotenv import load_dotenv


def add_entry():
    username = input("Enter the Username:")
    application = input("Enter the application:")
    password = getpass.getpass("Password:")
    cursor.execute(
        """
        INSERT INTO  keystore (
            username,
            application,
            password
        )
        VALUES(?, ?, ?)""",
        (username, application, password),
    )
    conn.commit()


def list_data(skip=False):
    for row in cursor.execute("SELECT * from keystore").fetchall():
        print(row)
    if not skip:
        time.sleep(7)
        os.system("clear")


def update_entry():
    list_data(True)
    sql_update_query = """
    Update keystore set username = ?, application = ?, password = ? where id = ?
    """
    id = input("Enter ID of entry you want to edit:")
    username = input("Enter the Username:")
    application = input("Enter the application:")
    password = getpass.getpass("Password:")
    columnValues = (username, application, password, id)
    cursor.execute(sql_update_query, columnValues)
    conn.commit()
    print("Record Updated successfully ")


def delete_entry():
    list_data(True)
    sql_query = """
    DELETE from keystore where id = ?
    """
    id = input("Which entry do you want to delete -> Enter ID:")
    cursor.execute(sql_query, id)
    conn.commit()
    print("Record Deleted successfully ")


def main():
    attemps = 0
    while attemps < 3:
        password = getpass.getpass("Please Enter the password ->")
        if password == GLOBAL_PASSWORD:
            if sys.argv[1] == "add":
                add_entry()
                break
            if sys.argv[1] == "list":
                list_data()
                break
            if sys.argv[1] == "update":
                update_entry()
                break
            if sys.argv[1] == "delete":
                delete_entry()
                break
        else:
            print("!!!!!Wrong Password!!!!")
            attemps += 1


if __name__ == "__main__":
    load_dotenv()
    GLOBAL_PASSWORD = os.getenv("GLOBAL_PASSWORD")
    conn = sqlite3.connect(
        "/home/haitham/Desktop/Training/password_manager/database.db"
    )
    cursor = conn.cursor()
    main()
    conn.close()
