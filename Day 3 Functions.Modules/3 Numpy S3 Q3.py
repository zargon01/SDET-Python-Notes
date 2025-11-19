import math 

def calculate_cone_volume():
    height = float(input())
    radius = float(input())

    v = math.pi * (radius**2) * (height/3)
    volume = round(v,2)
    print(volume)
if __name__ == "__main__":
    calculate_cone_volume()