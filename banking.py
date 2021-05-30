import random
import string
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
first_6 = 400000
count = 0
card = 0
pin = 0
card_number = None
pin_code = None
n = None
user_card = None
cur.execute('CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT,balance INTEGER DEFAULT 0)')
conn.commit()


def info():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    global n
    n = input()


def create_account():
    global n, count
    count += 1
    card_generate()
    print("""Your card has been created
Your card number:""")
    print(card)
    print("Your card PIN:")
    print(pin)
    info()
    user_input()


def card_generate():
    global first_6, card, pin
    size = 4
    chars = string.digits
    card_no = [int(i) for i in str(first_6)]
    card_num = [int(i) for i in str(first_6)]
    seventh_15 = random.sample(range(9), 9)
    for i in seventh_15:
        card_no.append(i)
        card_num.append(i)
    for t in range(0, 15, 2):
        card_no[t] = card_no[t] * 2
    for i in range(len(card_no)):
        if card_no[i] > 9:
            card_no[i] -= 9
    s = sum(card_no)
    mod = s % 10
    check_sum = 0 if mod == 0 else (10 - mod)
    card_num.append(check_sum)
    card_num = [str(i) for i in card_num]
    card = ''.join(card_num)
    pin = ''.join(random.choice(chars) for _i in range(size))
    cur.execute(f"INSERT INTO card(number, pin) VALUES ({card}, {pin})")
    conn.commit()
    return card, pin


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        _sum = (digit % 10) + (digit // 10)
        return _sum


def pass_luhn(recipient):
    # reverse the credit card number
    recipient = recipient[::-1]
    # convert to integer list
    recipient = [int(x) for x in recipient]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(recipient, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0


def log_in():
    global n, card_number, pin_code
    print('Enter your card number:')
    user_card_number = input('> ')
    print('Enter your PIN:')
    user_pin_code = input('> ')
    cur.execute('SELECT CAST(EXISTS (SELECT number || pin FROM card WHERE number = ? AND pin = ?) AS VARCHAR(2));',
                (user_card_number, user_pin_code))
    account_check = cur.fetchone()
    if '1' in account_check:
        print('You have successfully logged in!')
        card_number = user_card_number
        pin_code = user_pin_code
        successful_login()
    else:
        print('Wrong card number or PIN!')
        info()
        user_input()
        n = input()


def balance():
    balance = cur.execute('SELECT balance FROM card WHERE number = ? AND pin = ?', (card_number, pin_code)).fetchone()
    print("Balance: {}".format(balance[0]))
    conn.commit()


def add_income():
    print("Inter income:")
    income = int(input())
    cur.execute("UPDATE card SET balance = (balance + ?) WHERE number = ? AND pin = ?", (income, card_number, pin_code))
    conn.commit()
    print("Income was added!")


def do_transfer(card_number):
    row = get_account_info(card_number)
    print("Transfer")
    recipient = input("Enter card number:")
    if recipient == card_number:
        print("You can't transfer money to the same account!")
        successful_login()
    elif pass_luhn(recipient):
        cur.execute('SELECT * FROM card WHERE number=' + recipient)
        conn.commit()
        rec_row = cur.fetchone()
        if rec_row:  # record exist
            amount = int(input("Enter how much money you want to transfer:"))
            if amount < row[-1]:  # enough balance
                cur.execute("UPDATE card SET balance=(balance - ?) WHERE number = ? AND pin = ?", (amount, card_number, pin_code))
                conn.commit()
                cur.execute("UPDATE card SET balance=(balance + ?) WHERE number = ? ", (amount, recipient))
                conn.commit()
                print("Success!")
            else:  # When balance is not enough
                print("Not enough money!")
        else:  # When no record in db found
            print("Such a card does not exist.")
    else:  # When Luhn test fails
        print("Probably you made a mistake in the card number. Please try again!")
    successful_login()


def get_account_info(card_number):
    cur.execute('SELECT * FROM card WHERE number={}'.format(card_number))
    conn.commit()
    return cur.fetchone()


def close_account(card_number):
    cur.execute('DELETE FROM card WHERE number={}'.format(card_number))
    conn.commit()
    print("The account has been closed!")


def successful_login():
    global n
    print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
    n = input()
    if n == "1":
        balance()
        successful_login()
        n = input()
    elif n == "2":
        add_income()
        successful_login()
        n = input()
    elif n == "3":
        do_transfer(card_number)
        successful_login()
        n = input()
    elif n == "4":
        close_account(card_number)
        info()
        user_input()
    elif n == "5":
        print("You have successfully logged out!")
        info()
        user_input()
    elif n == "0":
        print("Bye!")
        exit()


def user_input():
    global n
    if n == "1":
        create_account()
    elif n == "2":
        log_in()

    elif n == "0":
        print("Bye!")
        exit()


info()
user_input()
