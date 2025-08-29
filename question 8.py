
#*   * * * *          
#_  * * * *        
#_ _ * * *         
#_ _ _*  *        

#_ _ _ _* 

n=int(input("enter the number: "))
 for i in range(n):
     for j in range(i):
         print("_", end=' ')
     for k in range(n-i):
         print("*",end=' ')
     print()
