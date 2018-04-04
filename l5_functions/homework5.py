import os
os.environ["CARD_TYPE"] = "Europe"
from l5_functions.my_first_package import my_functions
# my_functions.card_has_errors()
# my_functions.print_bank()

while True:
    card = input("Enter the credit card number in the format(XXXX XXXX XXXX XXXX):\n")
    card = card.split(" ")
    if my_functions.card_has_errors(card):
        print("Not valid card number!")
        continue
    if my_functions.print_bank(card):
        True
    break

from l5_functions.my_first_package import my_functions
# my_functions.date_check()

while True:
    mm_yy = input("Enter expiration date \"mm/yy\":\n")
    mm_yy = mm_yy.split("/")
    if len(mm_yy) != 2 or my_functions.date_check(mm_yy):
        print("Wrong format. Try again!")
    if mm_yy[0] > "0" and mm_yy[0] <= "12" and mm_yy[1] > "18":
        print("Successful")
    else:
        continue
    break

while True:
    cvv = input("Enter Card Verification Code:\n")
    if len(cvv) == 3:
        try:
            int(cvv)
        except ValueError:
            print("Error CVV")
            continue
    else:
        continue
    break
print("Your data has been accepted for processing. Please wait!")