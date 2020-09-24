print('(a)')

for row in range(0,10):

    for column in range(0,row+1):

        print("*",end='')
    print('')


print('(b)')

for row in range(10,0,-1):

    for column in range(0,row):

        print("*",end='')
    print('')




