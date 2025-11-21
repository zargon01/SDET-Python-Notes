class python_string():
    def __init__(self, string):
        self.string = string

    def reverse_words(self):
        reverse = []
        og_list = list(self.string.split())


        index = len(og_list)-1
        for i in range(0,len(og_list)):
            element = og_list[index]
            index-=1
            reverse.append(element)
        
        for item in reverse:
            print(f"{item}",end = " ")




def main():
    string = input()

    obj = python_string(string)
    obj.reverse_words()


if __name__ == "__main__":
    main()