messages = [
"A: Puh. Wie es hier aussieht!\nWo ist das Telefon?\nVielleicht in der Küche?",
"B: Nein. Hier ist kein Telefon!\nAber hier ist eine Uhr!",
"A: Oh, das ist die Uhr von Stefan, oder?",
"B: Stimmt! Ich schreibe Stefan.\nEr sucht die Uhr bestimmt...",
"A: Hmm, wo sind die Schlüssel?",
"B: Vielleicht im Wohnzimmer?",
"A: Nein, hier sind keine Schlüssel.",
"B: Ah, hier.",
"A: Super, danke.",
"A: Ah, es ist Stefans Uhr.\nAhm, Julia: Ist hier auch ein Rucksack?",
"B: Stefans Rucksack?\nNein. Tut mir leid.\nHier ist kein Rucksack."
]

def print_message(messages):
    for message in messages:
        print(f"{message}\n")

print_message(messages)
