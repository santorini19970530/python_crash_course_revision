favourite_places = {
    "steven" : ['tokyo', 'pusan', 'yokohama'],
    "apple" : ['new york', 'london'],
    "baka" : ['rome', 'frankfurt', 'seoul','taipei']
}

for name, places in favourite_places.items():
    print(f"{name.title()}\'s favourite place are:")
    for place in places:
        print(f"{place.title()}")
