import numpy as np
           

def string_case_transformations():
    string = input()
    lst = string.split()
    arr = np.array(lst)

    print(np.char.capitalize(arr))
    print(np.char.lower(arr))
    print(np.char.upper(arr))
    print(np.char.swapcase(arr))




if __name__ == "__main__":
    string_case_transformations()