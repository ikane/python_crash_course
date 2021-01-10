guests = ["Pierre", "Jacque", "Paul"]

print("I'd like to invite you " + guests[0])
print("I'd like to invite you " + guests[1])
print("I'd like to invite you " + guests[2])

print("-----------------------------------")
print("Jacque couldn't make unfortunatly!")

print("-----------------------------------")
del guests[1]
guests.insert(1, "Marie")

print("-----------------------------------")
print(guests)

print("-----------------------------------")
print("I find a bigger table!")

guests.insert(0, "Modou")
guests.insert(2, "Ibrahim")
guests.append("Christian")

print("-----------------------------------")
print(guests)

print("3-7-----------------------------------")
print("I'm sorry but i can invite only 2 people!")

guest = guests.pop()
print("I'm sorry " + guest + ", i cannot invite you to the dinner!")
guest = guests.pop()
print("I'm sorry " + guest + ", i cannot invite you to the dinner!")
guest = guests.pop()
print("I'm sorry " + guest + ", i cannot invite you to the dinner!")
guest = guests.pop()
print("I'm sorry " + guest + ", i cannot invite you to the dinner!")

print("-----------------------------------")
print(guests)

print("-----------------------------------")
print("You're still invited, " +  guests[0])
print("You're still invited, " +  guests[1])

del guests[0]
del guests[0]

print("------------ Guest List ----------------")
print(guests)
