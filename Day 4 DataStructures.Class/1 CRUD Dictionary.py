


def create_new_item(dict):
    key = input("Enter key:")
    value = input("Enter value: ")
    
    dict [key] = value
    return dict


def add_value(dict):
    key = input("Enter key:")
    value = input("Enter value to add: ")
    
    dict [key] = value
    return dict


def delete(dict):
    key = input("Enter the key you want to delete :")
    #del dict [key]
    #dict.popitem()   - pop last item
    #dict.clear()
    dict.pop(key)
    return dict
    
    
def display(dict):
    for k,v in dict.items():
        print("Key = {k}, Value = {v}.")
        
    for k in dict.keys():
        for v in dict.items(k):
            print(f"Key = {k}, Value = {v}")
            
    
    