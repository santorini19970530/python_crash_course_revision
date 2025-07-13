# Python Crash Course, 2Ed, writtern by Eric Matthes

members = []

countMember = 0

for count in range(6):
    person = {
        'nick_name' : 'eunha',
        'first_name' : 'eunbi',
        'last_name' : 'jung',
        'age' : 26,
        'city' : 'seoul'
    }
    members.append(person)

members[0]['first_name'] = 'sojung'
members[0]['last_name'] = 'kim'
members[0]['age'] = 27
members[0]['nick_name'] = 'sowon'

members[1]['first_name'] = 'yerin'
members[1]['last_name'] = 'jung'
members[1]['nick_name'] = 'yerin'

members[3]['first_name'] = 'yuna'
members[3]['last_name'] = 'choi'
members[3]['age'] = 25
members[3]['nick_name'] = 'yuju'

members[4]['last_name'] = 'hwang'
members[4]['age'] = 24
members[4]['nick_name'] = 'sinb'

members[5]['first_name'] = 'yewon'
members[5]['last_name'] = 'kim'
members[5]['age'] = 24
members[5]['nick_name'] = 'umji'

for member in members:
    countMember += 1
    print(f"I am going to talk about my wife no. {countMember}:\nHer name is {member['last_name'].title() + ' ' + member['first_name'].title()}.\nShe is {member['age']} years old.\nShe is living in {member['city'].title()}.")
    print("...\n")
