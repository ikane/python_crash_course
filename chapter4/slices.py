animals = ["dog", "parrot", "tortle", "cat", "mouse","hamster"]

print("The first three items are:" + str(animals[:3]))

middle = int(len(animals)/2)-1
end = middle + 3

print("Print three items from the middle:")

print(animals[middle:end])

print("The last three items in the list are:")

print(animals[-3:])

print("*************************************************")

pizzas = ["Orientale","chiken barbecue", "Spicy Hot One"]
friend_pizzas = pizzas[:]
pizzas.append("Basilica Poulet")
friend_pizzas.append("Urban Kebab")

print("My favorite pizzas are :" + str(pizzas))
print("My frend's favorite pizzas are :" + str(friend_pizzas))
