from random import choice
from string import digits
import random
import string
import re



#firstName = ("Aleksandr", "Andrey", "Gleb", "Yegor", "Igor", "Kirill", "Leonid")
lastName = ("Polischuk", "Voron", "Glasunov", "Smolenskiy", "Lifecell", "Petrov", "Ivanov")

error_elm_phone = ("[", "-", "]", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))
error_elm_card = ("-", " ", str(random.choice(string.ascii_lowercase + string.ascii_uppercase)))
#code = "+380"
code = ("+7", "+380")
number = (95, 66, 50, 44, 63, 98, 96, 97, 44)

def generated_input():
    person = (random.choice(firstName) + " " + random.choice(lastName))
    #########################
    phone = list(f"{random.choice(code)}{random.choice(number)}{''.join([random.choice(digits) for x in range(7)])}")
    if random.randint(1, 50) == 1:
        phone[random.randint(1, len(phone)-1)] = random.choice(error_elm_phone)
    phone = ''.join(phone)

    mounth = str(random.randint(1, 12))
    if len(mounth) == 1:
        mounth = '0'+ (mounth)

    yy = str(random.randint(18, 21))
    exp_day = mounth + '/' + yy

    card = list(''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)) +
                ''.join(choice(digits) for i in range(4)))

    if random.randint(1, 100) == 1:
        card[random.randint(0, len(card)-1)] = random.choice(error_elm_card)
    card = ''.join(card)
    card = card[0:4] + ' ' + card[4:8] + ' ' + card[8:12] + ' ' + card[12:16]
    cardholders = {"Name": person, "Phone": phone, "Exp_day": exp_day, "Card": card}
    return cardholders


def generatedPerson()



def check_credents(rand_cred):
    phone_cred = re.search(r'[a-zA-Z\[\]\-\ ]', rand_cred.get("Phone"))
    card_cred = re.search(r'[a-zA-Z\ ]', (rand_cred.get("Card")[0:4]+rand_cred.get("Card")[5:9]+rand_cred.get("Card")[10:14]+rand_cred.get("Card")[15:19]))
    if phone_cred or card_cred:
        return True
    else:
        return False
