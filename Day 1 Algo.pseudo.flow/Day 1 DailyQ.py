"""Problem Statement: Matrix Diagonal Sum
You are given a square matrix of size n × n. Write an algorithm to calculate the sum of both 
diagonals (primary and secondary). If an element belongs to both diagonals (center 
element in odd-sized matrix), count it only once.

Example Input
matrix = [
 [1, 2, 3],    1,1 + 1,3
 [4, 5, 6],    2,2
 [7, 8, 9]     3,1 + 3,3
]

Expected Output
Sum = 1 + 5 + 9 + 3 + 7 = 25"""


size = int(input())                    #nxn input

def matrixinput(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input())     #matrix input
            row.append(element)
            
        matrix.append(row)
    return matrix
        
        
def diagonalsum(matrix):
    
    n=len(matrix)
    sum = 0
    for i in range (n):
        sum += matrix[i][i]          #(1,1)(2,2)(3,3)
        sum += matrix[i][n-1-i]      #(1,2)(2,2)(3,2)
        print(sum)
    if n%2 == 1:
        sum = sum - matrix[n//2][n//2]    #(1,1)(2,2)(3,3)(1,2)(3,2)
        
    
    return sum
            
    
print(diagonalsum(matrixinput(size)))


