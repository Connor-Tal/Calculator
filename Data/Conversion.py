unit = input ("What would you like to convert? from US Standard to metric or metric to US Standard? ")
unit_lower = unit.lower()
if unit_lower == "US Standard to metric":
    operation = input ("Feet, Yards, Inches, Pounds, Kilograms, Fahrenheit, or Miles?")
    operation_lower = operation.lower()
    if operation_lower == "feet":
        feet = int(input("Enter the number of feet "))
        meter = feet / 3.2808
        centimeter = feet * 30.48
        print("The number of meters is " + str(meter))
        print("The number of centimeters is " + str(centimeter))
    if operation_lower == "yards":
        yards = int(input("Enter the number of yards "))
        meter = yards / 1.0936
        centimeter = yards * 91.44
        print("The number of meters is " + str(meter))
        print("The number of centimeters is " + str(centimeter))
    if operation_lower == "inches":
        inches = int(input("Enter the number of inches "))
        meter = inches / 39.3701
        centimeter = inches * 2.54
        print("The number of meters is " + str(meter))
        print("The number of centimeters is " + str(centimeter))
    if operation_lower == "pounds":
        pounds = int(input("Enter the number of pounds "))
        kilogram = pounds / 2.2046
        gram = pounds * 453.592
        print("The number of kilograms is " + str(kilogram))
        print("The number of grams is " + str(gram))
    if operation_lower == "kilograms":
        kilograms = int(input("Enter the number of kilograms "))
        pounds = kilograms / 0.453592
        gram = kilograms * 1000
        print("The number of pounds is " + str(pounds))
        print("The number of grams is " + str(gram))
    if operation_lower == "fahrenheit":
        fahrenheit = int(input("Enter the number of fahrenheit "))
        celsius = (fahrenheit - 32) * 5/9
        kelvin = (fahrenheit + 459.67) * 5/9
        print("The number of celsius is " + str(celsius))
        print("The number of kelvin is " + str(kelvin))
    if operation_lower == "miles":
        miles = int(input("Enter the number of miles per hour "))
        kilometers = miles / 1.60934
        meters = miles * 1609.34
        print("The number of kilometers is " + str(kilometers)) 
if unit_lower == "metric to US Standard":
    operation = input ("Meters, Centimeters, Kilograms, Grams, Celsius, or Kilometers?")
    operation_lower = operation.lower()
    if operation_lower == "meters":
        meters = int(input("Enter the number of meters "))
        feet = meters * 3.2808
        yards = meters * 1.0936
        inches = meters * 39.3701
        print("The number of feet is " + str(feet))
        print("The number of yards is " + str(yards))
        print("The number of inches is " + str(inches))
    if operation_lower == "centimeters":
        centimeters = int(input("Enter the number of centimeters "))
        feet = centimeters / 30.48
        yards = centimeters / 91.44
        inches = centimeters / 2.54
        print("The number of feet is " + str(feet))
        print("The number of yards is " + str(yards))
        print("The number of inches is " + str(inches))
    if operation_lower == "kilograms":
        kilograms = int(input("Enter the number of kilograms "))
        pounds = kilograms / 0.453592
        pounds = kilograms / 2.2046
        print("The number of pounds is " + str(pounds))
    if operation_lower == "grams":
        grams = int(input("Enter the number of grams "))
        pounds = grams / 453.592
        print("The number of pounds is " + str(pounds))
    if operation_lower == "celsius":    
        celsius = int(input("Enter the number of celsius "))
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        print("The number of fahrenheit is " + str(fahrenheit))
        print("The number of kelvin is " + str(kelvin))
    if operation_lower == "kilometers":
        kilometers = int(input("Enter the number of kilometers "))
        miles = kilometers * 1.60934
        miles = kilometers * 1609.34
        print("The number of miles is " + str(miles))
