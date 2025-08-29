#*        *
#**      **
#***    ***
#****  ****
#**********
#formula=2n-2i


n = 5  
for i in range(1, n + 1):
    print('*' * i, end='')
    space = (n - i) * 2
    print(' ' * space, end='')
    print('*' * i)
