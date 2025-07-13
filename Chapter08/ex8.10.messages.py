# Python Crash Course, 2Ed, writtern by Eric Matthes

from time import sleep

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

sent_messages = []

def send_message(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending below message:\n...\n{current_message}\n...")
        sent_messages.append(current_message)
        sleep(1)
        print("Message sent!\n")
    
print("Current mesages are:\n------\n")
print_message(messages)
send_message(messages[:], sent_messages)
print("------\nNow the messages are:\n------\n")
print_message(sent_messages)
