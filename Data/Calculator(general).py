print("A calculator with general functions")
opperation = input("What opperation would you like to do?")   
print("add, subtract, multiply, or divide")
print("You chose", opperation.lower())
opperation2 = opperation.lower()
if opperation2.__contains__("add"):
    number1 = input("What number would you like to add?")
    number2 = input("What number would you like to add to the first number?")
    total = int(number1) + int(number2)
    print(total)

if opperation2.__contains__("subtract"):
    number1 = input("What number would you like to subtract from?")
    number2 = input("What number would you like to subtract from the first number?")
    total = int(number1) - int(number2)
    print(total)

if opperation2.__contains__("multiply"):
    number1 = input("What number would you like to multiply?")
    number2 = input("What number would you like to multiply the first number by?")
    total = int(number1) * int(number2)
    print(total)

if opperation2.__contains__("divide"):
    number1 = input("What number would you like to divide?")
    number2 = input("What number would you like to divide the first number by?")
    total = int(number1) / int(number2)
    print(total)