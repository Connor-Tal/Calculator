print("A calculator with functions for income/intrest and bank")
what = input("income or intrest?")
print("You chose", what.lower())
what2 = what.lower()
if what2.__contains__("income"):
    earnings = input("how much are you earning?")
    tax = input("How much are you being taxed?")

    perecent = 1/float(tax)
    totaltax = float(earnings) * perecent
    total = float(earnings) - totaltax

    total2 = total.__round__(2)
    totaltax2 = totaltax.__round__(2)

    print("You will be taxed", totaltax2, "dollars, leaveing you with", total2, "dollars")

if what2.__contains__("intrest"):
    moneyin = float(input("How much money are you deposiing?"))
    intrest = input("What is the intrest rate?")
    years = input("How many years will the money be in the account?")

    math = 1/int(intrest)
    perecent = math * 100
    divided = moneyin * perecent *float(years)

    totalintrest = divided/100
    total = totalintrest + moneyin

    total2 = total.__round__(2)
    totalintrest2 = totalintrest.__round__(2)

    print("You will recive", totalintrest2, "total intrest, in the next", years, "years the account will have", total2, "dollars")
    moneyin = float(input("How much money are you deposiing?"))
    intrest = input("What is the intrest rate?")
    years = input("How many years will the money be in the account?")

    math = 1/int(intrest)
    perecent = math * 100
    divided = moneyin * perecent *float(years)

    totalintrest = divided/100
    total = totalintrest + moneyin

    total2 = total.__round__(2)
    totalintrest2 = totalintrest.__round__(2)

    print("You will recive", totalintrest2, "total intrest, in the next", years, "years the account will have", total2, "dollars")