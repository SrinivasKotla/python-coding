cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sort the given list permanently
cars.sort()
print(cars)

# Sort list in reverse order
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

print("Here is the list in reverse order:")
cars.reverse()
print(cars)

print("Length of cars list: "+str(len(cars)))

