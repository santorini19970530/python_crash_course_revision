cities = []

def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}.\n")

cityInsert = {
    'city_name' : 'osaka',
    'country' : 'japan'
}

cities.append(cityInsert)

cityInsert = {
    'city_name' : 'munich',
    'country' : 'germany'
}

cities.append(cityInsert)

cityInsert = {
    'city_name' : 'london',
    'country' : 'britain'
}

cities.append(cityInsert)

for city in cities:
    describe_city(city['city_name'], city['country'])
