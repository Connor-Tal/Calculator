true = True
add = False
delete = False
view = False
add2 = False
employee1 = False
employee2 = False
choise11 = False
Account1name = "NaN"
Account1password = "NaN"
Account2name = "NaN"
Account2password = "NaN"

while true == True:
    if choise11 == False:
        print("Welcome to the Employee Management System")
        choice1 = input("Would you like to add, view, or delete employees?")
        choice1_lower = choice1.lower()
        choise11 = True
    if choise11 == True:
        if choice1_lower == "add":
            add = True
        if choice1_lower == "view":
            view = True
        if choice1_lower == "delete":
            delete = True

        if add == True:
            print("Please enter this information to create an employee")
            Account1name = input("Enter account name ")
            Account1password = input("Enter account password ")
            full_name = input("Enter employee name ")
            email = input("Enter employee email ")
            position = input("Enter employee position ")
            salary = input("Enter employee salary ")
            person1 = Account1name, full_name, email, position, salary
            print(person1)
            print("Employee added")
            employee1 = True
            add = False
            choise2 = input("Would you like to cointinue adding employees, view, or delete employees?")
            choise2_lower = choise2.lower()
            if choise2_lower == "add":
                add2 = True
            if choise2_lower == "view":
                view = True
            if choise2_lower == "delete":
                delete = True
        if add2 == True:
            print("Please enter this information to create an employee")
            Account2name = input("Enter account name ")
            Account2password = input("Enter account password ")
            full_name1 = input("Enter employee name ")
            email1 = input("Enter employee email ")
            position1 = input("Enter employee position ")
            salary1 = input("Enter employee salary ")
            person2 = Account2name, full_name, email, position, salary
            print(person2)
            print("Employee added")
            employee2 = True
            add2 = False
            choise2 = input("Would you like to add, view, or delete employees?")
            choise2_lower = choise2.lower()
            if choise2_lower == "view":
                view = True
            if choise2_lower == "delete":
                delete = True
            if choise2_lower == "add":
                if employee1 == True and employee2 == False:
                    add2 = True
                if employee1 == False and employee2 == True:
                    add = True
                if employee1 == True and employee2 == True:
                    choise2 = input ("You have no more avalible employees to add. Would you like to view, or delete employees?")
                    choise2_lower = choise2.lower()
                    if choise2_lower == "view":
                        view = True
                    if choise2_lower == "delete":
                        delete = True
                if employee1 == False and employee2 == False:
                    add = True
        
        if view == True:
            user = input("Enter username of the account you would like to view ")
            if user == Account1name:
                passw = input("Enter password ")
                if passw == Account1password:
                    print(person1)
                    view = False
                    choise2 = input("Would you like to view another employee, add, or delete employees?")
                    choise2_lower = choise2.lower()
                    if choise2_lower == "view":
                        view = True
                    elif choise2_lower == "delete":
                        delete = True
                    elif choise2_lower == "add" and employee1 == False:
                        add = True
                    elif choise2_lower == "add" and employee1 == True:
                        add2 = True   
                else:
                    true = False
                    exit("Incorrect password")
    
            elif user == Account2name:
                passw = input("Enter password ")
                if passw == Account2password:
                    print(person2)
                    view = False
                    view = Fachoise2 = input("Would you like to view another employee, add, or delete employees?")
                    choise2_lower = choise2.lower()
                    if choise2_lower == "view":
                        view = True
                    elif choise2_lower == "delete":
                        delete = True
                    elif choise2_lower == "add" and employee1 == False:
                        add = True
                    elif choise2_lower == "add" and employee1 == True:
                        add2 = True

                else:
                    true = False
                    exit("Incorrect password")
            else:
                true = False
                print("User not found")

        if delete == True:
            user = input("Enter username of the account you would like to delete ")
            if user == Account1name:
                passw = input("Enter password ")
                if passw == Account1password:
                    del person1
                    print("Employee deleted")
                    delete = False
                    employee1 = False
                    choise2 = input("Would you like to continue deleting employees, view, or add employees?")
                    choise2_lower = choise2.lower()
                    if choise2_lower == "delete":
                        delete = True
                    elif choise2_lower == "view":
                        view = True
                    elif choise2_lower == "add" and employee1 == False:
                        add = True
                    elif choise2_lower == "add" and employee1 == True:
                        add2 = True
                else:
                    true = False
                    exit("Incorrect password")

            elif user == Account2name:
                passw = input("Enter password ")
                if passw == Account2password:
                    del person2
                    print("Employee deleted")
                    delete = False
                    employee2 = False
                    choise2 = input("Would you like to continue deleting employees, view, or add employees?")
                    choise2_lower = choise2.lower()
                    if choise2_lower == "delete":
                        delete = True
                    elif choise2_lower == "view":
                        view = True
                    elif choise2_lower == "add" and employee1 == False:
                        add = True
                    elif choise2_lower == "add" and employee1 == True:
                        add2 = True
                else: 
                    true = False
                    exit("Incorrect password")
            else:
                true = False
                print("User not found")     

    if choise2_lower == "exit":
        true = False
        exit("Thank you for using the program")
    if choice1_lower == "exit":
        true = False
        exit("Thank you for using the program")