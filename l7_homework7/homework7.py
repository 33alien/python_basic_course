import os
os.environ["CARD_TYPE"] = "China"
from l7_homework7.my_two_package import my_functions_1

region = os.environ["CARD_TYPE"] = "Europe"
region = os.environ.get("CARD_TYPE", "China")

if region == "Europe":
    card = my_functions_1.cardHasErrorsEurope()
else:
    card = my_functions_1.cardHasErrorsChina()

nameBank = my_functions_1.printBank(card)

mounthYear = my_functions_1.checkDate()

cvv = my_functions_1.checkCvv()

cardOwner = my_functions_1.checkCardholders()

file1 = open("DoneHomework7.txt", "w")
file1.write(f" Your data has been accepted for processing.\n Name: {cardOwner.upper()}\n"
             f" Credit Card: {card}\n MM/YY: {mounthYear}\n Cvv: {cvv}\n"
             f" Please wait!")
file1.close()
