def validate_input_positive(function):
    def wrapper(x,y,z):
        try:
            x != int(x)
            y != int(y)
            z != int(z)
        except:
            print(f"Error: Please enter valid numeric values.")
            print(f"Error: All arguments must be positive integers.")
            print("None")
            return
        if int(x) <= 0 or int(y) <= 0 or int(z) <= 0:
            print(f"Error: All arguments must be positive integers.")
            print("None")
            return

        function(x,y,z)

    return wrapper


@validate_input_positive
def calculate_cuboid_volume(length,width,height):
    l,w,h = float(length),float(width),float(height)
    volume = float(l*w*h)
    print(volume)


def main():
    length = input()
    width = input()
    height = input()

    calculate_cuboid_volume(length,width,height)

if __name__ == "__main__":
    main()