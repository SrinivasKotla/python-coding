motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Alter value at a index code
# motorcycles[0] = 'ducati'
# print(motorcycles)


# Appending values to list
motorcycles.append('ducati')
print(motorcycles)

# Inserting elements in a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Deleting a element from the list
del motorcycles[0]
print("Deleting - " + str(motorcycles))

popped_motorcycle = motorcycles.pop()
print("Motorcycles after popping - " + str(motorcycles))
print("Pooped motorcycle is " + popped_motorcycle.title())



