# Python Crash Course, 2Ed, writtern by Eric Matthes

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

# from starr to 4
print(players[:4])

# start from 2
print(players[2:])

# last three players
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
