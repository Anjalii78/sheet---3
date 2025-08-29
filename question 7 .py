n = 5  # number of lines

for i in range(1, n + 1):
    spaces = '_' * (n - i)
    stars = '*' * i
    print(spaces + stars)
#____*
#___**
#__***
#_****
#*****
