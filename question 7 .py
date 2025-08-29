'''
 _ _ _ _*        
 _ _ _ * *           
 _ _ *  * *           
 _  * *  * * 
*  * *  * *   
'''





n=int(input("enter the number "))
for i in range(1,n+1):
     for j in range (n-i):
         print("_", end=" ")
     for k in range(i):
         print("*",end=" ")
     print()
   
