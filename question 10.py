#*        *
#**      **
#***    ***
#****  ****
#**********
#formula=2n-2i
n = 5  # Number of rows

for i in range(1, n + 1):
    stars = i
    spaces = (n - i) * 2

    print("*" * stars + " " * spaces + "*" * stars)
