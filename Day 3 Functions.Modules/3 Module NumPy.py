import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([[1,2][3,4]])
arr.size
np.zeros((3,3))
np.ones((3,3))

arr[0]  #first value
arr[-1] #last value

arr[1:4]  #slicing gives index 1,2,3

np.sum(arr)
np.max(arr)
np.mean(arr)