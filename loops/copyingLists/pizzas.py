my_pizzas = ["Cheese Pizaa", "Barbeque pizza", "Pepperoni pizza"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("Meat pizza")
friend_pizzas.append("Veggie pizza")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)