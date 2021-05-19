from helper import *
from db import *


class Card:
    def __init__(self):
        self.id = ""
        self.number = ""
        self.pin = ""
        self.balance = 0

    def create_card(self):
        card_number = generate_card()
        card_pin = generate_pin()
        card_id = get_count()
        data = (card_id, card_number, card_pin, 0)
        insert_card(data)
        self.set_card(data)

    def set_card(self, data):
        self.id = data[0]
        self.number = data[1]
        self.pin = data[2]
        self.balance = data[3]

    def print_credit_card(self):
        print("Your card number:")
        print(self.number)
        print("Your card PIN:")
        print(self.pin)

    def add_balance(self, balance):
        self.balance += balance
        update_balance(balance, self.number)

    def transfer_balance(self, balance, card_number):
        current_card_number = self.number
        current_card_balance = balance * -1
        update_balance(current_card_balance, current_card_number)

        other_card_number = card_number
        other_card_balance = balance
        update_balance(other_card_balance, other_card_number)
