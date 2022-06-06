print("A calculator with general functions")
print("add, subtract, multiply, divide, or exponent")
opperation = input("What opperation would you like to do?")   
print("You chose", opperation.lower())
opperation2 = opperation.lower()
if opperation2.__contains__("add"):
    number1 = input("What number would you like to add?")
    number2 = input("What number would you like to add to the first number?")
    total = float(number1) + float(number2)
    print(total)

if opperation2.__contains__("subtract"):
    number1 = input("What number would you like to subtract from?")
    number2 = input("What number would you like to subtract from the first number?")
    total = float(number1) - float(number2)
    print(total)

if opperation2.__contains__("multiply"):
    number1 = input("What number would you like to multiply?")
    number2 = input("What number would you like to multiply the first number by?")
    total = float(number1) * float(number2)
    print(total)

if opperation2.__contains__("divide"):
    number1 = input("What number would you like to divide?")
    number2 = input("What number would you like to divide the first number by?")
    total = float(number1) / float(number2)
    print(total)

if opperation2.__contains__("exponent"):
    number1 = input("What number would you like to exponentiate?")
    number2 = input("What number would you like to exponentiate the first number by?")
    total = float(number1) ** float(number2)
    print(total)

