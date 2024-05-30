dictionary = {}
def displayMenu():
    print("-----Storing Names & Birthdays-----")
    print("\n1. Look up a birthday\n2. Add a new birthday" +
          "\n3. Change a birthday\n4. Delete a birthday\n5. Quit the Program")

def lookUp():
    name = input("\nEnter the name you want to look up: ")

    if name in dictionary:
        print(f'{dictionary.get(name)} is the birthday for {name}')
    else:
        print(f"That name wasn't found")

def addNew():
    name = input("\nEnter your friend's name: ")
    bDay = input("Enter their Birthday: ")

    dictionary[name] = bDay

def changeBday():
    name = input("\nEnter the name you want to select: ")
    if name in dictionary:
        bDay = input("Enter the new birthday: ")
        dictionary[name] = bDay
    else:
        print("\nThat name wasn't found")

def delBday():
    name = input("\nEnter the name you want to delete: ")
    dictionary.pop(name, 'Name not found')

def main():
    displayMenu()
    choice = int(input("\nPlease enter a number between 1 and 5: "))

    while choice < 1 or choice > 5:
        choice = int(input("\nEnter a valid input: "))

    while choice != 5:
        displayMenu()
        if choice == 1:
            lookUp()
        elif choice == 2:
            addNew()
        elif choice == 3:
            changeBday()
        elif choice == 4:
            delBday()

        for key, value in dictionary.items():
            print(key, value, end = " ")
        print(" ")
        choice = int(input("\nPlease enter a number between 1 and 5: "))
    print("\nExiting Program")


if __name__ == '__main__':
    main()