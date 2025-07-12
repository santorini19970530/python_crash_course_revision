# update_dinner.py -- some of the members cannot come to dinner, so invite again them to the my dinner

invitation = ", would you join my dinner tonight?"

gfriend = ['sowon', 'yerin', 'eunha', 'yuju', 'sinb', 'umji']
print(f"Current list: {gfriend}")
print(f"{gfriend[0]}{invitation}")
print(f"{gfriend[1]}{invitation}")
print(f"{gfriend[2]}{invitation}")
print(f"{gfriend[3]}{invitation}")
print(f"{gfriend[4]}{invitation}")
print(f"{gfriend[5]}{invitation}")

print("\n---")
print(f"{gfriend[1]} cannot come to my dinner. But IU can.")
gfriend[1] = 'IU'
print(f"Current list: {gfriend}")


