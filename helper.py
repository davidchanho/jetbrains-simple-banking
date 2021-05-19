import random


def option_menu(options):
    def print_options():
        for option in options.values():
            print(option["label"])

    def execute_option():
        cmd = input()
        return options[cmd]['action']()

    while True:
        print_options()
        execute_option()


def generate_pin():
    pin = random.randint(0000, 9999)
    return str(pin).ljust(4, '0')


def generate_card_number():
    issuer_number = "400000"
    customer_account = str(random.randint(000000000, 999999999))
    card_number = issuer_number + customer_account
    return int(card_number.ljust(16, '0'))


def generate_card():
    card_number = generate_card_number()
    if is_checksum_valid(card_number):
        return str(card_number)
    else:
        checksum = get_checksum(card_number)
        return str(card_number + (10 - checksum % 10))


def get_checksum(number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum


def is_checksum_valid(number):
    checksum = get_checksum(number)
    if checksum % 10 == 0:
        return True
