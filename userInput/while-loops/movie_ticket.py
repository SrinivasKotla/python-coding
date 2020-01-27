prompt = "\nPlease enter you age:"
prompt += "\n(Enter 'quit' to exit.) "

while True:
    message = input(prompt)
    if message == 'quit':
        break

    message = int(message)
    price = 0
    if message < 3:
        price = 0
    elif message <= 12:
        price = 10
    elif message > 12:
        price = 15
    print("\nYour ticket price is $" + str(price))

