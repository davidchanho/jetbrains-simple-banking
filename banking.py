import sys
from Card import Card
from helper import *
from db import *

initialize_db()
mycard = Card()


def menu():
    options = {
        "1": {"label": "1. Create an account", "action": create_menu},
        "2": {"label": "2. Log into account", "action": login_menu},
        "0": {"label": "0. Exit", "action": exit_menu},
    }
    option_menu(options)


def create_menu():
    mycard.create_card()
    print("Your card has been created")
    mycard.print_credit_card()
    menu()


def login_menu():
    while True:
        login_number = input("Enter your card number:\n")
        login_pin = input("Enter your PIN:\n")
        login = load_from_db(login_number, login_pin)
        if login:
            mycard.set_card(login)
            print("You have successfully logged in!")
            user_menu()
        else:
            print("Wrong card number or PIN!")
            menu()


def exit_menu():
    print("Bye!")
    sys.exit()


def user_menu():
    options = {
        "1": {"label": "1. Balance", "action": balance_menu},
        "2": {"label": "2. Add income", "action": income_menu},
        "3": {"label": "3. Do transfer", "action": transfer_menu},
        "4": {"label": "4. Close account", "action": close_account},
        "5": {"label": "5. Log out", "action": logout_menu},
        "0": {"label": "0. Exit", "action": exit_menu},
    }
    option_menu(options)


def balance_menu():
    print("Balance: ", mycard.balance)
    user_menu()


def income_menu():
    amount = int(input("Enter income:"))
    mycard.add_balance(amount)
    print("Income was added!")
    user_menu()


def invalid_checksum():
    print("Probably you made a mistake in the card number.")
    print("Please try again!")
    user_menu()


def invalid_card():
    print("Such a card does not exist.")
    user_menu()


def invalid_amount():
    print("Not enough money!")
    user_menu()


def valid_amount(amount, card_number):
    mycard.transfer_balance(amount, card_number)
    print("Success!")
    user_menu()


def transfer(card_number):
    print("Enter how much money you want to transfer:")
    amount = int(input("Enter how much money you want to transfer:"))
    if amount > mycard.balance:
        invalid_amount()
    else:
        valid_amount(amount, card_number)


def transfer_menu():
    print("Transfer")
    card_number = input("Enter card number:\n")
    existing_card = is_existing_card(card_number)
    checksum_valid = is_checksum_valid(card_number)

    if not checksum_valid:
        invalid_checksum()

    if not existing_card:
        invalid_card()

    if checksum_valid and existing_card:
        transfer(card_number)


def close_account():
    delete_card(mycard.number)
    menu()


def logout_menu():
    print("You have successfully logged out!")
    menu()


def main():
    menu()


main()
