n = int(input("Enter the value of n: "))
star = 1
space=int(n/2)
for k in range (n-space):
    for j in range(space):
        print(" ",end = "")
    space-=1
        
    for i in range (star):
        print("*", end="")
    star+=2 
    print("")
        
    
"""    
   * 
  ***
 *****
*******
"""