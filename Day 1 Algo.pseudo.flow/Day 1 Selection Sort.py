def take_arr(n):
    arr = []
    for i in range (n):
        n = int(input("Enter num: "))
        arr.append(n)
    return arr

def selection_sort(arr):
    for i in range (len(arr)):
        swapindex = i
        for j in range (i,len(arr)):
            if arr[j]<arr[swapindex]:
                swapindex = j
        temp = arr[i]
        arr[i] = arr[swapindex]
        arr[swapindex]=temp
    return arr
        
    
n = int(input("Enter len of array: "))
print(selection_sort(take_arr(n)))