
def sort_names():
    list = []
    n = int(input())
    for i in range (n):
        dict = {}
        dict["Name"]= input()
        list.append(dict)
    list.sort(key = lambda x: x["Name"])
    print(list)




if __name__ == "__main__":
    sort_names()