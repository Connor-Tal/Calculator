way = input("Which way would you like to sort? (ascending or descending)")
way_lower = way.lower()
if way_lower == "ascending":
    print("Ascending")
    data = input("Enter the data you would like to sort:")
    if data.__contains__(","):
        count = data.count(",")
        for i in range(count):
            data_list = data.split(",")
            
        print(sorted(data_list))
    
    else:
        exit("Error: Data must be separated by a comma")
elif way_lower == "descending":
    print("Descending") 
    data = input("Enter the data you would like to sort:") 
    if data.__contains__(","):
        count = data.count(",")
        for i in range(count):
            data_list = data.split(",")
        
        print(sorted((data_list), reverse=True))
    
    else:
        exit("Error: Data must be separated by a comma")
else:
    exit("No valid input")