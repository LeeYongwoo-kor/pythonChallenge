import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.iban.com/currency-codes")
soup = BeautifulSoup(result.text, "html.parser")

countryTable = soup.find("table", {"class": "downloads"})
tbody = countryTable.find("tbody")
lecords = tbody.findAll("tr")

tableInf = []

for lecord in lecords:
    lecordInf = {}
    columns = lecord.findAll("td")
    for index, column in enumerate(columns, start=1):
        if index % 4 == 1:
            lecordInf["country"] = column.string.capitalize()
        elif index % 4 == 2:
            lecordInf["currency"] = column.string
        elif index % 4 == 3:
            lecordInf["code"] = column.string
        elif index % 4 == 0:
            lecordInf["number"] = column.string
    if not lecordInf["code"]:
        continue
    tableInf.append(lecordInf)

print("Hello! Please choose select a country by number:")
for index, country in enumerate(tableInf):
    print("# ", index, tableInf[index]["country"])

while True:
    try:
        answer = int(input("#: "))
        if answer >= 0 and answer < len(tableInf):
            print("You chose", tableInf[answer]["country"])
            print("The currency code is", tableInf[answer]["code"])
            break
        else:
            print("Choose a number from the list.")
    except:
        print("That wasn't a number.")