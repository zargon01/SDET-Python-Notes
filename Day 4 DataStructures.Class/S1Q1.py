def square_elements():
    sep_list = list(map(int,input().split()))
    square = []
    for number in sep_list:
        square.append(number*number)
    print(f"List of Squares: {square}")

if __name__ == "__main__":
    square_elements()