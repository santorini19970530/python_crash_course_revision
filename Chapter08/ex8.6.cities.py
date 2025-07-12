cities = []

def describe_city(city, country):
    print(f"{city.title()}, {country.title()}")

def city_country(city, country):
    city_insert = {}
    city_insert['city_name'] = city.lower()
    city_insert['country'] = country.lower()
    cities.append(city_insert)

city_country('OsAka', 'japan')
city_country('berlin', 'germAny')
city_country('paris', 'FrancE')

for city in cities:
    describe_city(city['city_name'], city['country'])
