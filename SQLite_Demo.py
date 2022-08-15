import sqlite3
from random import randint

global db
global sql

db = sqlite3.connect("server.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()


def reg():
    user_login = input("Login: ")
    user_password = input("Password: ")

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()
    else:
        print("This data exists")

        for value in sql.execute("SELECT * FROM users"):
            print(value)


def delter_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    db.commit()

    print("GOOODBYE!!!")


def casino():
    global user_login

    user_login = input("Log in: ")
    number = randint(1, 2)

    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        print("No such one. Register, pleaes")
        reg()
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = {balance + 1000} WHERE login = '{user_login}'")
            db.commit()
        else:
            delter_db()
            print("YOU lose")


def enter():
    sql.execute("SELECT login, cash FROM users")
    row = sql.fetchall()[0][0]
    print(row)


def main():
    casino()
    enter()


if __name__ == "__main__":
    main()
    db.close()
