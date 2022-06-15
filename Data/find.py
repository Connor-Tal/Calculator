import random
import string
import time
import timeit

n = 0
b = 0


print("This will print random numbers and or words of a certain length, and what trial number, until it finds the number or word you want.")
print("WARNING: This program can take a long time to run, is resource intensive and will not finish if you enter a number that is too high, or misspell a word.")
question = input("Find a word or a number?")
question2 = question.lower()

if question2.__contains__("word"): 
   time.sleep(1)
   lines = open("/usr/share/dict/words").read().splitlines()
enter = input("What would you like to do? find a specific word, or find a random word?")
enter2 = enter.lower()
if enter2.__contains__("random"):
    word = random.choice(lines)
    a=[]
    e = 0 
    n = 1000000000000000000000000000000000000000000000000000000000000000000000000
    start = timeit.default_timer()

    for j in range(n):
        word2 = random.choice(lines)
        e = e + 1
        print ("Trials", e, "Word:", word2)
    
        if word == word2:
            print ("You found the word", word, "in", e, "trials")
            stop = timeit.default_timer()
            execution_time = stop - start
            print("Program Executed in "+str(execution_time))
            break
else:
    words = input("What word would you like to find?")
    a=[]
    e = 0
    n = 1000000000000000000000000000000000000000000000000000000000000000000000000
    start = timeit.default_timer()

    for j in range(n):
        word2 = random.choice(lines)
        e = e + 1
        print ("Trials", e, "Word:", word2)

        if words == word2:
            print ("You found the word", words, "in", e, "trials")
            stop = timeit.default_timer()
            execution_time = stop - start
            print("Program Executed in "+str(execution_time))
            break


if question2.__contains__("number"):
    a=[]
    e = 0 
    a =int(input("Lowest number?"))
    b = int(input("Highest number?"))
    d = input("What number do you want to find?")
    time.sleep(1)
    n = 1000000000000000000000000000000000000000000000000000000000000000000000000
    start = timeit.default_timer()
    for j in range(n):
        e = e + 1
        print ("Trials", e, "Number:", random.randint(int(a),int(b)))
        if random.randint(int(a),int(b)) == int(d):
            print ("You found the number", d, "in", e, "trials")
            stop = timeit.default_timer()
            execution_time = stop - start

            print("Program Executed in "+str(execution_time))
            break