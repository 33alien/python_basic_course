card = input("Enter your number card number (16):\n")                       # Enter the 16 digit numeric code
if len(card) == 16:
    try:
        card = int(card)
        print("Successful")
    except:
        exit()
else:
    exit()
mm, yy = input("Enter expiration date \"mm/yy\":\n").split("/")      # Required format "mm/yy"
try:
    if not len(mm) == 2 or not len(yy) == 2 or int(mm) < 1 or int(mm) > 12 or int(yy) < 0:
        exit()
    else:
        print("OK")
except ValueError:
    exit()
cvv = input("Enter Card Verification Code:\n")                              # Enter the 3-valued code
if len(cvv) != 3:
    try:
        cvv = int(cvv)
        print("Eroor!")
    except:
        exit()
else:
    print("Ha-ha ha. Now I will use your credit card!")



