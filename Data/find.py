import random
import string
import time
n = 0
b = 0

question = input("Find a word or a number?")
if question.__contains__("word"): 
    word = input("What is the word you want to find?")
    letter = int(input("How many letters are in the word?"))

    while b == 0:
        n = n + 1
        letters = string.ascii_lowercase
        x = "".join(random.sample(str(letters), int(letter)))
        print("Trial", int(n), "Word:", str(x))
        if x == word:
            print("You found the word", word, "in", n, "trials")
            break

if question.__contains__("number"):
    x = 1
    a = 0
    time.sleep(1)
    low = int(input("What would you like the lowest number to be?"))
    high = int(input("What would you like the highest number to be?"))
    target = int(input("What number do you want to find?"))
    while x == 1:
        a = a + 1
        number = random.randint(low,high)
        print("Trials:", a, "Number:", number)
        if number == target:
            print("You found the number", target, "in", a, "trials")       
            break