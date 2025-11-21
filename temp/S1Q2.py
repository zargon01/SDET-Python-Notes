class Person:
    
    def __init__(self, name, current_age):
        self.name = name
        self.__age = current_age

    def getAge(self):
        return self.__age
    
    def setAge(self,new_age):
        self.__age = new_age

def main():
    name = input()
    current_age = int(input())
    new_age = int(input())

    obj = Person(name,current_age)

    print(f"Name: {obj.name}")
    print(f"Age: {obj.getAge()}")
    obj.setAge(new_age)
    print(f"Updated Age: {obj.getAge()}")


if __name__ == "__main__":
    main()