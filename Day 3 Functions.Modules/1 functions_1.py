#create 4 functions
"""take user input as choice

add(a,b) with param, with returntype

div(user input in it)  no parameter, with returntype

mul  with parameter, no returntype
print in the function only

sub no parameter no returntype
no parameter and print there"""


def addition(num1,num2):
    sum=num1+num2
    return sum

def division():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    div = num1/num2
    return div,num1,num2

def multiplication(num1,num2):
    mul = num1*num2
    print(f"Multiplication of {num1} and {num2} is {mul}.")

def subtraction():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sub = num1-num2
    print(f"Subtraction of {num1} and {num2} is {sub}.")


choice = int(input("Enter your choice (1-4): "))

def main():
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum of {num1} and {num2} is {addition(num1,num2)}.")
        
    elif choice == 2:
        div,num1,num2= division()
        print(f"Division of {num1} and {num2} is {div}.")

    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        multiplication()
        
    elif choice == 4:
        subtraction()
    else:
        print("Dumb Choice. Try again")
    
#------------Main Code--------------
    
main()
    