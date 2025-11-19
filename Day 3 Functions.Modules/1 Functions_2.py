'''
INPUT- 
string
choice 

1 - no of vowels  (string) return count of vowels
2 - replace space with @
3 - convert whole to lower
4 - everything to upper

should not stop until exit (5)
'''


def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for i in string:
        if i in vowels:
            count+=1
    return count
        
def replace_space(string):
    out=""
    for i in string:
        if i == " ":
            out += "@"
        else:
            out += i
    return out

def lower_case(string):
    lower = string.lower()
    return lower

def upper_case(string):
    upper = string.upper()
    return upper
        
        


def main():
    string = input("Enter a string: ")
    choice = int(input("Enter a choice: "))
    
    while choice != 5:
        
        if choice == 1:
            print(f"No of vowels in the string {string} are {count_vowels(string)}")
        elif choice ==2:
            print(f"New string after replacing space with @ : {replace_space(string)}")
        elif choice ==3:
            print(f"New string after converting to lower : {lower_case(string)}")
        elif choice ==4:
            print(f"New string after converting to upper : {upper_case(string)}")
        else:
            print("Wrong choice dude")
            
        choice = int(input("Enter a new choice: "))

main()