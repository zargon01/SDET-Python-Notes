class Country:
    def __init__(self,name,countryCode,isdCode):
        self.name = name
        self.countryCode = countryCode
        self.isdCode = isdCode

    def display_info(self):
        print(f"Country Name:{self.name}")
        print(f"Country Code:{self.countryCode}")
        print(f"ISD Code:{self.isdCode}")


def main():
    name = input()
    countryCode = input()
    isdCode = input()

    obj = Country(name, countryCode, isdCode)

    obj.display_info()



if __name__ == "__main__":
    main()