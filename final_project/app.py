import csv

from final_project.utils._1 import *

header = ["Name", "Phone", "Exp_day", "Card"]
records = []

for i in range(100):
    records.append(createRecord())

cardholdersFile = open("cardholders.csv", "w")
cardholdersFile = csv.DictWriter(cardholdersFile, fieldnames=header)
cardholdersFile.writeheader()
cardholdersErrorFile = open("cardholders_error.csv", "w")
cardholdersErrorFile = csv.DictWriter(cardholdersErrorFile, fieldnames=header)
cardholdersErrorFile.writeheader()

for i in range(len(records)):
    if not checkCredents(records[i]):
        cardholdersFile.writerow({"Name": records[i].get("Name"), "Phone": records[i].get("Phone"),
                                  "Exp_day": records[i].get("Exp_day"), "Card": records[i].get("Card")})
    else:
        cardholdersErrorFile.writerow({"Name": records[i].get("Name"), "Phone": records[i].get("Phone"),
                                       "Exp_day": records[i].get("Exp_day"), "Card": records[i].get("Card")})
