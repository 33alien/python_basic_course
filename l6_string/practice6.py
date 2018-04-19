import re


# name = "bohdan polishchuk"
# print(name[::-1])
# print(name.title())
phone_number = +380995556677
matched = re.match(r'^\+[0-9]{12}$', phone_number)
print(matched)
    if matched:
        print("1234")
    








