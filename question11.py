#merge the code prevoius 6th and 7th
#**********
#****  ****
#***    ***
#**      **
#*        *
#*        *
#**      **
#***    ***
#****  ****
#**********

n = 10  # Total number of rows

for i in range(n):
    if i < n // 2:
        stars = n // 2 - i
        spaces = i * 2
    else:
        stars = i - n // 2 + 1
        spaces = (n - i - 1) * 2

    print("*" * stars + " " * spaces + "*" * stars)


    
