"""
create a list globally
in that list store dictionary
in that dictionary (id, name, age)


case 1 add
if id is already present
say id already already exist otherwise, add the dictionary and say student added successfully with ID:--

case 2 update
take ID
check if it exists or not
if exists then take name and age and update and say updated successfully
else id does not exist

case 3 remove
based on id delete whole dict

case 4 display


ID = 101, Name = "Golu", Age = 13.0
ID = 102, Name = "CR", Age = 23.0


case 5 exit
Exiting Student management system

any other case invalid choice?
"""

def add_id(list):
    ID = int(input("Enter your ID: "))
    for item in list:
        if item["ID"] == ID:
            print(f"{ID} already exists.")
            return
    else:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        
        dict={"ID": ID, "Name": name, "Age":age} 
        list.append(dict)
        
    return list




def update_id(list):
    ID = int(input("Enter your ID Number: "))
    for item in list:
        if item["ID"] == ID:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            item["Name"] = name
            item["Age"] = age
            return
    print(f"{ID} does not exist.")
        
        
        

def remove_id(list):
    ID = int(input("Enter your ID Number to remove: "))
    for item in list:
        if item["ID"] == ID:
            list.remove(item)
            print(f"{ID} removed successfully.")
            return
    print(f"{ID} not found.")


def display_id(list):
    for item in list:
        print(f"ID: {item["ID"]}, Name: {item["Name"]}, Age: {float(item["Age"])}")





def main(student_data):
    while True:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_id(student_data)
        elif choice == 2:
            update_id(student_data)
        elif choice == 3:
            remove_id(student_data)
        elif choice == 4:
            display_id(student_data)
        elif choice == 5:
            print("Exiting Student management system.")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    student_data = []
    main(student_data)