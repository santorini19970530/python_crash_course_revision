# update_dinner.py -- some of the members cannot come to dinner, so invite again them to the my dinner

invitation = ", would you join my dinner tonight?"

gfriend = ['sowon', 'yerin', 'eunha', 'yuju', 'sinb', 'umji']
print(f"Current list: {gfriend}, {len(gfriend)} dinner mates.")
print(f"{gfriend[0]}{invitation}")
print(f"{gfriend[1]}{invitation}")
print(f"{gfriend[2]}{invitation}")
print(f"{gfriend[3]}{invitation}")
print(f"{gfriend[4]}{invitation}")
print(f"{gfriend[5]}{invitation}")

print("\n---")
print(f"{gfriend[1]} cannot come to my dinner. But IU can.")
gfriend[1] = 'IU'

print("\n---")
print("and Sinb will bring WJSN come.")
gfriend.append("WJSN")
print(f"Current list: {gfriend}, {len(gfriend)} dinner mates.")

print("also, Eunha will bring another SinB to the dinner.\nThe two SinBs need to sit together.")
gfriend.insert(4, "Sinb")
print(f"Current list: {gfriend}, {len(gfriend)} dinner mates.")

print("\n---")
print("Now one SinB kicks another out.")
del gfriend[4]
print(f"Current list{gfriend}, {len(gfriend)} dinner mates.")

print("\n---")
print("Eunha is being dissed. She is sad and she left for crying.")
gfriend.remove("eunha")
print(f"Current list:{gfriend}, {len(gfriend)} dinner mates.")

print("\n---")
print(f"{gfriend.pop(0)} goes to comfort Eunha.")
print(f"Current list: {gfriend}, {len(gfriend)} dinner mates.")


