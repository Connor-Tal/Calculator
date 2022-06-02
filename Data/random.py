import random
import time
import string

question = input("Random number or word?")

if question.__contains__("number"):    
    time.sleep(1)
    low = int(input("What would you like the lowest number to be?"))
    high = int(input("What would you like the highest number to be?"))
    choise = random.randint(low,high)
    print (choise)
else:
    time.sleep(1)
    word = input("How many letters are in the word?")
    letters = string.ascii_lowercase
    x = "".join(random.sample(str(letters), str(word)))
    print (x)