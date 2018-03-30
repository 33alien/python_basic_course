myBool = True

while myBool:
    myBool = False
    card = input("Enter the credit card number in the format(XXXX XXXX XXXX XXXX):\n").split(' ')

    for i in card:
        if len(i) == 4:
            try:
                i = int(i)
            except:
                myBool = True
                break
        else:
            myBool = True
            break

if card[0] == "5167":
    print("You use PrivatBank credit card")
elif card[0] == "5375":
    print("You use Monobank credit card")
else:
    print("You use credit card from the unknown bank")

numbers = True

while numbers:
    numbers = False
    mm_yy = input("Enter expiration date \"mm/yy\":\n").split("/")

    for i in mm_yy:
        if len(i) == 2:
            try:
                i = int(i)
            except:
                numbers = True
                break
        else:
            numbers = True
            break

if mm_yy[0] > "0" and mm_yy[0] <= "12":
     if mm_yy[1] > "18":
        print("Successful")
else:
    print("Enter expiration date \"mm/yy\":\n")

while True:
    cvv = input("Enter Card Verification Code:\n")

    if len(cvv) == 3:
        try:
            cvv = int(cvv)
        except ValueError:
            print("Error")
            continue
    else:
        continue
    break
print("Your data has been accepted for processing. Please wait!")