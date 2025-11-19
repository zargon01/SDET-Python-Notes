def take_arr(n):
    arr = []
    for i in range (n):
        n = int(input("Enter num: "))
        arr.append(n)
    return arr

def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

print(bubbleSort(take_arr(5)))
