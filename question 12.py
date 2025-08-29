
#1
#12
#123
#1234



n = int(input("Enter no. of rows : "))
count = 0
for i in range(1, n+1): 
    count = 0
    for j in range(0, i):
        count += 1
        print(count, end=" ")
    print()
