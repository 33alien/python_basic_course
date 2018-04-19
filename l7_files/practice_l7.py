my_text = '''Hi,

Work123 work work
I am a Python developer and I want to work in a cool team.
I would like to get a chance to work in your company.
My work experience isn’t big enough, but I am an open minded person and ready to work hard.


Best regards,


{first_name} {last_name}'''

a1 = input()
a2 = input()

my_text = my_text.format(first_name = a1, last_name = a2)
print(my_text)

with open("python_text" , "w") as f:
    f.write(my_text)

with open("python_text" , "r") as f_read:
    result = 0
    result2 = 0
    for line in f_read:
        result += line.lower().count("work")
        result2 += line.upper().count("Work")
    print(result2)
