# Python Crash Course, 2Ed, writtern by Eric Matthes

glossary = {
    'die Adresse' : "address",
    'die Webseite' : "website",
        'können' :  "can",
    'Velen Dank' : "Very thnks"
}

for word, meaning in glossary.items():
    print(f"{word.title()} means {meaning.title()}.")
