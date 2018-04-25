from random import choice
from string import digits
import string
import random
import re

def createRecord():
    cardholders = {"Name": createPerson(), "Phone": createPhoneNumber(),
                   "Exp_day": createDate(), "Card": createCardNumber()}
    return cardholders


def createPerson():
    firstName = ("Aleksandr", "Andrey", "Gleb", "Yegor", "Igor", "Kirill", "Leonid")
    lastName = ("Polischuk", "Voron", "Glasunov", "Smolenskiy", "Lifecell", "Petrov", "Ivanov")
    person = (random.choice(firstName) + " " + random.choice(lastName))
    return person

def createPhoneNumber():
    errorPhoneSymbol = ("[", "-", "]", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))
    code = ("+790", "+380")
    number = (95, 66, 50, 44, 63, 98, 96, 97, 44)

    phone = list(f"{random.choice(code)}{random.choice(number)}{''.join([random.choice(digits) for x in range(7)])}")
    if random.randint(1, 50) == 1:
        phone[random.randint(1, len(phone)-1)] = random.choice(errorPhoneSymbol)
    phone = ''.join(phone)
    return phone

def createDate():
    mounth = str(random.randint(1, 12))
    if len(mounth) == 1:
        mounth = '0'+ (mounth)

    yy = str(random.randint(18, 21))
    date = mounth + '/' + yy
    return date

def createCardNumber():
    errorCardSymbol = ("-", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))

    card = list(''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)))

    if random.randint(1, 100) == 1:
        card[random.randint(0, len(card)-1)] = random.choice(errorCardSymbol)
    card = ''.join(card)
    card = card[0:4] + ' ' + card[4:8] + ' ' + card[8:12] + ' ' + card[12:16]
    return card

def checkCredents(object):
    phoneCredents = re.search(r'[a-zA-Z\[\]\-\ ]', object.get("Phone"))
    cardCredents = re.search(r'[a-zA-Z\ ]', (object.get("Card")[0:4] + object.get("Card")[5:9]
                                             + object.get("Card")[10:14] + object.get("Card")[15:19]))
    if phoneCredents or cardCredents:
        return True
    else:
        return False
