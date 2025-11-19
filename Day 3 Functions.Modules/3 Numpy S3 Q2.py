import pandas as pd

def filter_passed_students():
    names = input().split()
    marks = list(map(int,input().split()))

    df = pd.DataFrame({'Name': names, 'Marks': marks})

    passed = df[df["Marks"]>=40]
    print(passed)

if __name__ == "__main__":
    filter_passed_students()