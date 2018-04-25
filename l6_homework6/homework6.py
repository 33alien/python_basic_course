import os
os.environ["CARD_TYPE"] = "China"
from l6_homework6.my_first_package import my_functions

region = os.environ["CARD_TYPE"] = "Europe"
region = os.environ.get("CARD_TYPE", "China")

if region == "Europe":
    card = my_functions.cardHasErrorsEurope()
else:
    card = my_functions.cardHasErrorsChina()

nameBank = my_functions.printBank(card)

mounthYear = my_functions.checkDate()

cvv = my_functions.checkCvv()

cardOwner = my_functions.checkCardholders()

print("Your data has been accepted for processing. Please wait!")
