guests = ['Sachin', 'Dhoni', 'Kohli']
print("Hi "+guests[0]+". I cordially invite you for my birthday party")
print("Hi "+guests[1]+". I cordially invite you for my birthday party")
print("Hi "+guests[2]+". I cordially invite you for my birthday party")

print(guests[2]+' is unable to attend the party')
guests[2] = 'Rohit'

print("Hi "+guests[0]+". I cordially invite you for my birthday party")
print("Hi "+guests[1]+". I cordially invite you for my birthday party")
print("Hi "+guests[2]+". I cordially invite you for my birthday party")

guests.insert(0, 'Dhawan')
guests.insert(2, 'Raina')
guests.append('Bumrah')

print("Hi "+guests[0]+". I cordially invite you for my birthday party")
print("Hi "+guests[1]+". I cordially invite you for my birthday party")
print("Hi "+guests[2]+". I cordially invite you for my birthday party")
print("Hi "+guests[3]+". I cordially invite you for my birthday party")
print("Hi "+guests[4]+". I cordially invite you for my birthday party")
print("Hi "+guests[5]+". I cordially invite you for my birthday party")

print("The dinner table isn't gonna delivered on time. So we can only have 2 guests")

removedGuest = guests.pop()
print("Sorry "+ removedGuest+". I am unable to invite you to the dinner")
removedGuest = guests.pop()
print("Sorry "+removedGuest+". I am unable to invite you to the dinner")
removedGuest = guests.pop()
print("Sorry "+removedGuest+". I am unable to invite you to the dinner")
removedGuest = guests.pop()
print("Sorry "+removedGuest+". I am unable to invite you to the dinner")

print("Hi "+guests[0]+". I cordially invite you for my birthday party")
print("Hi "+guests[1]+". I cordially invite you for my birthday party")

del guests[0]
del guests[0]
print(guests)
