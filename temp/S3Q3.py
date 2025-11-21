
def validate_input(func):
    def wrapper(n):
        try:
            n=int(n)
        except:
            print("Error: Please enter a valid integer.")
            print("Error: The argument must be a positive integer.")
            print("None")
            return
        if n<=0:
            print("Error: The argument must be a positive integer.")
            print("None")
            return
        func(n)
    return wrapper

@validate_input
def calculate_square(n):
    result = []
    for i in range (1,n+1):
        result.append(i*i)
    print(result)

def main():
    n = input()
    calculate_square(n)


if __name__ == "__main__":
    main()