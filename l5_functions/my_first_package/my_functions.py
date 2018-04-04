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
        return True
    return sens

def print_bank(card):
    if card[0] == "5167":
     print("You use PrivatBank credit card")
    elif card[0] == "5375":
     print("You use Monobank credit card")
    else:
     print("You use credit card from the unknown bank")

def date_check(mm_yy):
    for i in mm_yy:
        if len(i) == 2:
            try:
                i = int(i)
            except ValueError:
                return True
        else:
            return True
    return False
