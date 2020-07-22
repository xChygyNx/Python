# Write your code here
import createAccount
import logAccount

createAccount.create_db()
while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    command = input()
    if command == "1":
        createAccount.create_card()
    elif command == "2":
        logAccount.log_in()
    elif command == "0":
        print("Bye!")
        break
