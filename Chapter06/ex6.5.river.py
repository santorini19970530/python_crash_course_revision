rivers = {
    'nile' : "egypt",
        'eunha' : "Jung Eun Bi",
    'komogawa' : "japan"
}
countRiver = 0
countCountry = 0

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    countRiver += 1
    print(f"River {countRiver}: {river.title()}")

for country in rivers.values():
    countCountry += 1
    print(f"Country {countCountry}: {country.title()}")
