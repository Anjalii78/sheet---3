#**********
#****  ****
#***    ***
#**      **
#*        *


n = 5  # Number of rows

for i in range(n, 0, -1):
    stars = i
    spaces = (n - i) * 2

    print("*" * stars + " " * spaces + "*" * stars)



n=5
i=1
#formula used 2i-2
star=n-1+1
space=2-i-2
star=n-1+1
n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end="")

