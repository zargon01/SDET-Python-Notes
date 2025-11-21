"""
choice 1 - add a data (company name) if success then print company added successfully
choice 2 - update only if the company name is already present or print name is not available(which name, what name to update)
choice 3 - delete (name) if deleted then print deleted successfully or no data found
choice 4 - display Company details : then company name : {name} company name : {name}
choice 5 - print exiting from crud
"""


def add_data(list):
    value = input("Enter the name of company: ")
    if value in list:
        print(f"{value} already exists.")
    else:
        list.append(value)
        print(f"Compant {value} added successfully.")
    return list


def update_data(list):
    old = input("Enter name to replace: ")
    if old not in list:
        print(f"{new} Company does not exist.")
    else:
        new = input("Enter the new name: ")
        index = list.index(old)
        list[index]=new
        print(f"Company {new} updated.")
    return list

def delete_data(list):
    value = input("Enter the Company you want to delete: ")
    list.remove(value)
    if value in list:
        print(f"{value} deleted successfully.")
        list.remove(value)
    else:
        print(f"{value} not found.")
    return list

def display_data(list):
    print("Company details :")
    for text in list:
        print(f"Company name: {text}")
    

if __name__ == "__main__":
    list = []
    while True:
        print("----------------------------------")
        print("Choice 1 - Add data \nChoice 2 - Update data\nChoice 3 - Delete data\nChoice 4 - Display Data\nChoice 5 - Exit")
        print("----------------------------------")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_data(list)
        elif choice == 2:
            update_data(list)
        elif choice == 3:
            delete_data(list)
        elif choice ==4:
            display_data(list)
        elif choice == 5:
            list.clear()
            print("Exiting from CRUD.")
            break
        else:
            print("Invalid Choice")
        