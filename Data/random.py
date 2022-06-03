import random
import time
import string

print("Will output a random number or a random string of letters, of a cetian length.")
question = input("Random number or word?")

if question.__contains__("number"):    
    time.sleep(1)
    low = int(input("What would you like the lowest number to be?"))
    high = int(input("What would you like the highest number to be?"))
    choise = random.randint(low,high)
    print (choise)

if question.__contains__("word"):
    time.sleep(1)
    word = int(input("How many letters are in the word?"))
    letters = string.ascii_lowercase
    x = "".join(random.sample(str(letters), int(word)))
    print(str(x))