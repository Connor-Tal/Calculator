a = False
b = False

view = False
add = False
add2 = False
delete = False


class employee():
    def __init__(self, name, age, email, phone, address, position, salary):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        self.position = position
        self.salary = salary
    
print("Welcome to the employee management program")
print("Would you like to add, remove, or view employees?")
choice = input("Add, remove, or view employees?")
choice2 = choice.lower()
if choice2.__contains__("add") and a == False:
    add = True    
        
while add == True:        
    print("Create a user")
    person1 = {}
    person2 = {}
    aname = input("Enter account name ") 
    person1 = (aname)
    print("Enter information for", aname)
    name = input("Enter name ")
    age = input("Enter age ")
    email = input("Enter email ")
    phone = input("Enter phone number ")
    address = input("Enter address ")
    position = input("Enter position ")
    salary = input("Enter salary ")
    a = True
    print("User created")
    person1 = employee(name, age, email, phone, address, position, salary)
    print(person1.name)
    print(aname)
    user2 = input(" create a second?")
    user2 = user2.lower()
    if user2.__contains__("yes"):
        add2 = True
    else:
        add = False
        choise5 = input("Contuine?")
        choise5 = choise5.lower()
        if choise5.__contains__("yes"):
            choice3 = input("View or remove employees?")
            choice4 = choice3.lower()
            if choice4.__contains__("view"):
                view = True
            if choice4.__contains__("remove"):
                delete = True
        else:
            exit()

elif choice2.__contains__("remove") and a == True:
    choise6 = input("Remove employee? or create a new employee?")
    choise6 = choise6.lower()
    if choise6.__contains__("remove"):
        delete = True
    if choise6.__contains__("create"):
        add = False
        user2 == "yes" and b == False
     

if user2 == "yes" and b == False:
    add2 = True
while add2 == True:    
    aname1 = input("What is the name of the second employee? ")
    person2 = (aname1)
    print("Enter information for", aname1)
    name1 = input("Enter name ")
    age1 = input("Enter age ")
    email1 = input("Enter email ")
    phone1 = input("Enter phone number ")
    address1 = input("Enter address ")
    position1 = input("Enter position ")
    salary1 = input("Enter salary ")
    person2 = employee(name1, age1, email1, phone1, address1, position1, salary1)
    print(person2.name)
    print(aname1)
    print("User created")
    print("Max users is 2")
    b = True
    add = False
    
    choice3 = input("View or remove employees?")
    choice4 = choice3.lower()
    if choice4.__contains__("view"):
        view = True
    if choice4.__contains__("remove"):
        delete = True
    
    
else:
    choice3 = input("View or remove employees?")
    choice4 = choice3.lower()
    if choice4.__contains__("view"):
        view = True
    if choice4.__contains__("remove"):
        delete = True



if choice2.__contains__("remove"):
    delete = True
    
while delete == True:
    print("Remove a user")
    print("Enter the name of the user you would like to remove")
    delname = input("Enter name (Case sensitive): ")
    print("Are you sure you want to remove", delname, "?")
    answer = input("Yes or No? ")
    answer2 = answer.lower()
    if answer2 == "yes":
        print("User removed")
        if delname == person1:
            a = False
            del person1
        if delname == person2:
            b = False
            del person2
        else:
            print("User not found")
        
    else:
        print("User not removed")

if choice2.__contains__("view"):
    view = True
while view == True:
    print("View a user")
    print("Enter the name of the user you would like to view")
    viewname = input("Enter name (Case sensitive): ")
    if viewname == "person1":
        print(person1.name)
        print(person1.age)
        print(person1.email)
        print(person1.phone)
        print(person1.address)
        print(person1.position)
        print(person1.salary)
    if viewname == "person2":
        print(person2.name)
        print(person2.age)
        print(person2.email)
        print(person2.phone)
        print(person2.address)
        print(person2.position)
        print(person2.salary)
