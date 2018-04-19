import csv

from final_project.utils._1 import *

ls = []
for i in range(100):
    ls.append(generated_input())

with open("cardholders.csv", "w", newline= "") as cardholders_csv:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_csv, fieldnames= header)
    writer.writeheader()
    for i in range(len(ls)):
        if not check_credents(ls[i]):
            writer.writerow({"Name": ls[i].get("Name"), "Phone": ls[i].get("Phone"), "Exp_day": ls[i].get("Exp_day"), "Card": ls[i].get("Card")})

with open("cardholders_error.csv", "w", newline="") as cardholders_error_csv:
    header = ["Name", "Phone", "Exp_day", "Card"]
    writer = csv.DictWriter(cardholders_error_csv, fieldnames= header)
    writer.writeheader()
    for i in range(len(ls)):
        if check_credents(ls[i]):
            writer.writerow({"Name": ls[i].get("Name"), "Phone": ls[i].get("Phone"), "Exp_day": ls[i].get("Exp_day"), "Card": ls[i].get("Card")})