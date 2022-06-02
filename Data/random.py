import random

print("A random number generator")
low = int(input("What would you like the lowest number to be?"))
high = int(input("What would you like the highest number to be?"))
choise = random.randint(low,high)
print (choise)
