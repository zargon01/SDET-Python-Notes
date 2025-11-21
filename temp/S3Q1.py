def validate_input(function):
    def wrapper(a,b):
        try:
            a = int(a)
            b = int(b)
        except:
            print("Error: Please enter valid integers.")
            print("Error: All arguments must be positive integers.")
            print("None")
            return
        if a<=0 or b<=0:
            print("Error: All arguments must be positive integers.")
            print("None")
            return
        function(a,b)
    return wrapper

@validate_input
def multiply_numbers(a,b):
    c = int(a)*int(b)
    print(c)

def main():
    num1 = input()
    num2 = input()

    multiply_numbers(num1,num2)

if __name__ == "__main__":
    main()