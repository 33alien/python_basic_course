import os
def card_has_errors(card_number):
    sens = True
    region = os.environ.get("CARD_TYPE", "Europe")
    print(region)
    code_lenth = 4
    if region == "China":
        code_lenth = 3
    if len(card_number) == code_lenth:
        for i in card_number:
            if len(i) == 4:
                try:
                    i = int(i)
                    sens = False
                except ValueError:
                    return True
            else:
                return True
    else:
        return False
    return sens

def print_bank(card):
    if card[0] == "5167":
     print("You use PrivatBank credit card")
    elif card[0] == "5375":
     print("You use Monobank credit card")
    else:
     print("You use credit card from the unknown bank")
#
# def date_check(mm_yy):
#     for i in mm_yy:
#         if len(i) == 2:
#             try:
#                 i = int(i)
#             except ValueError:
#                 return True
#         else:
#             return True
#     return False
while True:
    card = input("Enter the credit card number in the format(XXXX XXXX XXXX XXXX):\n")
    card = card.split(" ")
    if card_has_errors(card):
        print("Not valid card number!")
        continue
    if print_bank(card):
        True
    break

# while True:
#     mm_yy = input("Enter expiration date \"mm/yy\":\n")
#     mm_yy = mm_yy.split("/")
#     if len(mm_yy) != 2 or date_check(mm_yy):
#         print("Wrong format. Try again!")
#     if mm_yy[0] > "0" and mm_yy[0] <= "12" and mm_yy[1] > "18":
#         print("Successful")
#     else:
#         continue
#     break
#
# while True:
#     cvv = input("Enter Card Verification Code:\n")
#     if len(cvv) == 3:
#         try:
#             int(cvv)
#         except ValueError:
#             print("Error CVV")
#             continue
#     else:
#         continue
#     break
# print("Your data has been accepted for processing. Please wait!")