num = input("Type a number: ")
num = int(num)

if num % 10 == 0:
    print("Yes, " + str(num) + " is a multiple of 10")
else:
    print(str(num) + " is not a multiple of 10")