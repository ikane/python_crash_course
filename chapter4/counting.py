for value in range(1,11):
    print(value)

print("\n$$$$$$$$$$$$$\n")

million = list(range(1,1000000))

print("Min: " + str(min(million)))
print("Max: " + str(max(million)))
print("Sum: " + str(sum(million)))

print("======== Odd numbers ===========")
for odd in range(1,20, 2):
    print(odd)

print("======== Multiple of three using List compensation ===========")
multiples = [3 * value for value in range(3,30)]
print(multiples)

print("======== Cubes using List compensation ===========")
cubes = [c**3 for c in range(1,10)]
print(cubes)
