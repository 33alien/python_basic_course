import re

def cardHasErrorsEurope():
    while True:

        card = input(str("Enter the credit card number in the format(XXXX XXXX XXXX XXXX):\n"))
        credit = re.match(r'^\d{4}\ \d{4}\ \d{4}\ \d{4}$', card)
        if credit is None:
            continue
        else:
            return card
        break

def cardHasErrorsChina():
    while True:

        card = input(str("Enter the credit card number in the format(XXXX XXXX XXXX XXXX):\n"))
        credit = re.match(r'^\d{4}\ \d{4}\ \d{4}$', card)
        if credit is None:
            continue
        else:
            return card
        break

def printBank(card):

    if card.startswith('5167'):
        print("You use PrivatBank credit card")
    elif card.startswith('5375'):
        print("You use Monobank credit card")
    else:
        print("You use credit card from the unknown bank")

def checkDate():
    while True:

        mounthYear = input(str("Enter expiration date MM/YY:\n"))
        mY = re.match(r'[00-12]{2}\/[18-99]{2}$', mounthYear)
        if mY is True:
            continue
        else:
            return mounthYear
        break

def checkCvv():
    while True:

        cvv = input("Enter Card Verification Code:\n")
        dateCvv = re.match(r'[000-999]{3}$', cvv)
        if dateCvv is True:
            continue
        else:
            return cvv
        break

def checkCardholders():
    while True:

        cardOwner = input("Enter the name and second name of the cardholder:\n")
        patternOwner = re.match(r'[aA-zZ]+\ [aA-zZ]+$', cardOwner)
        if patternOwner is True:
            continue
        else:
            return cardOwner
        break