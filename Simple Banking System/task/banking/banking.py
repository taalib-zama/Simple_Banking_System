 # Write your code here
# pseudo menu part.
import random


class Card():
    data = {}

    def __init__(self, card_no, card_pin):  # here the key will be card no :
        self.card_no = card_no
        self.card_pin = card_pin
        self.balance = 0
        Card.data[card_no] = [self.card_pin, self.balance]

    def login(user_card_no, user_card_pin):
        if len(user_card_no) == 16 and len(user_card_pin) == 4:

            if user_card_no in Card.data.keys():
                #print((Card.data[user_card_no][0]))
                if Card.data[user_card_no][0] == user_card_pin:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def balance_check(card_no):
        return Card.data[user_card_no][1]


def n_len_rand(len_, floor=1):
    top = 10**len_
    if floor > top:
        raise ValueError(f"Floor {floor} must be less than requested top {top}")
    return f'{random.randrange(floor, top):0{len_}}'
# Luhn algorithms used to validate the generated account number.
def luhn_method(num):  # here num is in str format.
    # multiplying odd digits by 2.
    multiplied = ''
    for i in range(len(num)):
        if i % 2 == 0:  # selecting odd places starting from index = 0
            x = 2 * int(num[i])
            if x > 9:
                x = x - 9
                multiplied = multiplied + str(x)
            else:
                multiplied = multiplied + str(x)
        else:
            multiplied = multiplied + num[i]

    sum = 0
    for digit in multiplied:
        sum += int(digit)
    control_no = 0
    if (sum % 10 != 0):
        control_no = (10 - sum % 10)
    return (str(control_no))

menu1 = '''1. Create an account
2. Log into account
0. Exit'''
menu2 = '''1. Balance
2. Log out
0. Exit'''
flag = True
while (flag == True):
    print(menu1)
    in1 = int(input())
    if in1 == 1:
        # creating a random acc. no and PIN :
        acc_identifier = random.randint(000000000,999999999)  # Account identifier is a random 9-digit number unique for every user.
        num = str(400000000000000 + acc_identifier)  # 400000 is the fixed BIN (Bank identification number) for our bank.
        rand_pin = n_len_rand(4)
        rand_no = num + luhn_method(num)

        new = Card(rand_no,rand_pin)  # calling card class constructor for card creation with attributes as randon to be generated kater in code.
        print("Your card has been created")
        print("Your card number:")
        print(new.card_no)
        print("Your card PIN")
        print(new.card_pin)

    if in1 == 2:
        print("Enter your card number:")
        user_card_no = input()
        print("Enter you PIN:")
        user_card_pin = input()
        # check using the login function of class card and return a flag.
        login_flag = Card.login(user_card_no, user_card_pin)
        if login_flag == False:
            print("Wrong card number or PIN!")
            continue
        print("You have successfully logged in!")
        while (login_flag == True):

            print(menu2)
            in2 = int(input())
            if in2 == 1:
                # check balance using balance function of card class.
                # print(balance)
                print("Balance: 0")
            if in2 == 2:
                login_flag = False
                print("You have succesfully logged out")
            if in2 == 0:
                flag = False
                print("Bye!")
                break
    if in1 == 0:
        print("Bye!")
        flag = False
