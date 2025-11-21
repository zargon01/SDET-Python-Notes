
class Compare:
    def __init__(self, value):
        self.value = value

    def __gt__(self,other):
        self.value>other.value








def main():
    value1 = int(input())
    value2 = int(input())

    one = Compare(value1)
    two = Compare(value2)

    print(value1>value2)



if __name__ == "__main__":
    main()