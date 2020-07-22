import sqlite3
import sys


def get_rec(conn, card_num):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM card WHERE number like " + card_num)
    rec = cursor.fetchone()
    return rec


def log_in():
    print("Enter your card number:")
    num = input()
    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM card WHERE number like " + num)
    rec = cursor.fetchone()
    print("Enter your PIN:")
    pin = input()
    if rec is not None and rec[2] == pin:
        print("You have successfully logged in!")
        enter_card(conn, rec)
    else:
        print("Wrong card number or PIN!")
    conn.close()


def enter_card(conn, rec):
    while True:
        print("1. Balance")
        print("2. Add income")
        print("3. Do transfer")
        print("4. Close account")
        print("5. Log out")
        print("0. Exit")
        command = input()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM card WHERE number like " + rec[1])
        account = cursor.fetchone()
        if command == "1":
            print()
            print("Balance: ", account[3])
            print()
        elif command == "2":
            exec_income(conn, account)
        elif command == "3":
            exec_transfer(conn, account)
        elif command == "4":
            delete_account(conn, account)
            break
        elif command == "5":
            print("You have successfully logged out!")
            break
        elif command == "0":
            sys.exit()


def exec_income(conn, account):
    print()
    print("Enter income:")
    income = input()
    cursor = conn.cursor()
    cursor.execute("UPDATE card SET balance = balance + " + income +
                   " WHERE number like " + account[1])
    conn.commit()
    print("Income was added!")
    print()


def luhn_check(card_num):
    sum_ = 0
    for i in range(15):
        digit = int(card_num[i])
        if i % 2 == 0:
            digit *= 2
            if digit >= 10:
                digit -= 9
        sum_ += digit
    if (sum_ + int(card_num[15])) % 10 != 0:
        return False
    return True


def exec_transfer(conn, src_account):
    print()
    print("Transfer")
    print("Enter card number:")
    dst_card_num = input()
    if len(dst_card_num) != 16 or (not luhn_check(dst_card_num)):
        print("Probably you made mistake in the card number. Please try again!")
        return
    elif src_account[1] == dst_card_num:
        print("You can't transfer money to the same account!")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM card WHERE number like " + dst_card_num)
    dst_account = cursor.fetchone()
    if dst_account is None:
        print("Such a card does not exist.")
        return
    print("Enter how much money you want to transfer:")
    transfer = int(input())
    if transfer > int(src_account[3]):
        print("Not enough money!")
        return
    cursor.execute("UPDATE card SET balance = balance - " + str(transfer) +
                   " WHERE number = " + src_account[1])
    cursor.execute("UPDATE card SET balance = balance + " + str(transfer) +
                   " WHERE number = " + dst_account[1])
    conn.commit()
    print("Success")
    print()


def delete_account(conn, account):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM card WHERE number = " + account[1])
    conn.commit()
    print("The account has been closed!")
