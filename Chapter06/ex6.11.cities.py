# Python Crash Course, 2Ed, writtern by Eric Matthes

cities = {
    'tokyo' : { 
        'country' : 'japan',
    'population' : 1_000_000,
        'food' : 'sushi'},
    'new york' : {
        'country' : 'the unided states',
        'population' : 2_000_000,
        'food' : 'hamburger'
    },
    'hongkong' : {
        'country' : 'hongkong',
        'population' : 6_000_000,
        'food' : 'noodles'
    }
}

for city, information in cities.items():
    print(f"Information of {city.title()}:")
#    for country, population, food in information.items():
    print(f"Country: {information['country'].title()}\nPopulation: {information['population']}\nFamous food :{information['food'].title()}\n")
