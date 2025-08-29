#1
#1*
#1*3
#1*3*
#1*3*5


line = ''
num = 1
for i in range(1, 6):
    if i % 2 == 0:
        line += '*'
    else:
        line += str(num)
        num += 2
    print(line)
