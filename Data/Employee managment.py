add = False
view = False
delete = False

employee1 = False
employee2 = False

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
choise = input("Would you like to add, remove, or view employees?")
choise_lower = choise.lower()
if choise_lower.__contains__("add"):
    add = True
if choise_lower.__contains__("view"):
    view = True
if choise_lower.__contains__("remove"):
    delete = True

while add == True and  employee1 == False:
    print("Create a user")
    person1 = {}
    username = input("Enter account name ")
    person1 = (username)
    print("Enter information for", username)
    name = input("Enter name ")
    age = input("Enter age ")
    email = input("Enter email ")
    phone = input("Enter phone number ")
    address = input("Enter address ")
    position = input("Enter position ")
    salary = input("Enter salary ")
    print("User created")
    person1 = employee(name, age, email, phone, address, position, salary)
    employee1 = True
    add = False
    addmore = input("Create a second user?")
    addmore_lower = addmore.lower()
    if addmore_lower.__contains__("yes"):
        print("Create a user")
        person2 = {}
        username2 = input("Enter account name ")
        person2 = (username2)
        print("Enter information for", username2)
        name1 = input("Enter name ")
        age1 = input("Enter age ")
        email1 = input("Enter email ")
        phone1 = input("Enter phone number ")
        address1 = input("Enter address ")
        position1 = input("Enter position ")
        salary1 = input("Enter salary ")
        print("User created")
        person2 = employee(name1, age1, email1, phone1, address1, position1, salary1)
        employee2 = True
        choice3 = input("View or remove employees?")
        choice3_lower = choice3.lower()
        if choice3_lower.__contains__("view"):
            view = True
        if choice3_lower.__contains__("remove"):
            delete = True
       
    if addmore_lower.__contains__("no"):
        add = False
        choice3 = input("View or remove employees?")
        choice3_lower = choice3.lower()
        if choice3_lower.__contains__("view"):
            view = True
        if choice3_lower.__contains__("remove"):
            delete = True
        
while add == True and employee2 == False and employee1 == True:
    print("Create a user")
    person2 = {}
    username2 = input("Enter account name ")
    person2 = (username2)
    print("Enter information for", username2)
    name1 = input("Enter name ")
    age1 = input("Enter age ")
    email1 = input("Enter email ")
    phone1 = input("Enter phone number ")
    address1 = input("Enter address ")
    position1 = input("Enter position ")
    salary1 = input("Enter salary ")
    print("User created")
    person2 = employee(name, age, email, phone, address, position, salary)
    employee2 = True
    add = False
    choice3 = input("View or remove employees?")
    choice3_lower = choice3.lower()
    if choice3_lower.__contains__("view"):
        view = True
    if choice3_lower.__contains__("remove"):
        delete = True

while add == True and employee2 == True and employee1 == True:
    exit("You have reached the maximum number of users")

else:
    choice3 = input("View or remove employees?")
    choice3_lower = choice3.lower()
    if choice3_lower.__contains__("view"):
        view = True
    if choice3_lower.__contains__("remove"):
        delete = True

while view == True:
    inputuser = input("Enter account name ")
    if inputuser == username:
        print(person1.name)
        print(person1.age)
        print(person1.email)
        print(person1.phone)
        print(person1.address)
        print(person1.position)
        print(person1.salary)
        view = False
        choise10 = input("Would you like to view another user?")
        choise10_lower = choise10.lower()
        if choise10_lower.__contains__("yes"):
            view = True
        if choise10_lower.__contains__("no"):
            view = False
            choise5 = input("Would you like to add, or delete employees?")
            choise5_lower = choise5.lower()
            if choise5_lower.__contains__("add"):
                add = True
            if choise5_lower.__contains__("delete"):
                delete = True
                
    if inputuser == username2:
        print(person2.name)
        print(person2.age)
        print(person2.email)
        print(person2.phone)
        print(person2.address)
        print(person2.position)
        print(person2.salary)
        view = False
        choise10 = input("Would you like to view another user?")
        choise10_lower = choise10.lower()
        if choise10_lower.__contains__("yes"):
            view = True
        if choise10_lower.__contains__("no"):
            view = False
            choise5 = input("Would you like to add, or delete employees?")
            choise5_lower = choise5.lower()
            if choise5_lower.__contains__("add"):
                add = True
            if choise5_lower.__contains__("delete"):
                delete = True
    else:
        print("User not found")
        view = False
        choise5 = input("add or delete employees, or try again?")
        choise5_lower = choise5.lower()
        if choise5_lower.__contains__("add"):
            add = True
        if choise5_lower.__contains__("delete"):
            delete = True
        if choise5_lower.__contains__("try"):
            view = True

while delete == True:
    inputuser = input("Enter account name ")
    if inputuser == username:
        print("User deleted")
        employee1 = False
    if inputuser == username2:
        print("User deleted")
        employee2 = False
    else:
        print("User not found")
        delete = False
        choise5 = input("add or view employees, or try again?")
        choise5_lower = choise5.lower()
        if choise5_lower.__contains__("add"):
            add = True
        if choise5_lower.__contains__("view"):
            view = True
        if choise5_lower.__contains__("try"):
            delete = True
