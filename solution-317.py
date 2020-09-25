print('(a)')

for row in range(0,10):

    for column in range(0,row+1):

        print("*",end='')
    print('')


print('\n(b)')

for row in range(10,0,-1):

    for column in range(0,row):

        print("*",end='')
    print('')

print('\n(c)')

row=1
while(row<=10):
    col=1
    while(col<=10):
        if(col<row):
            print(' ',end='')
        else:
            print('*',end='')
        col+=1
    row+=1
    print('')

print('\n(d)')

r=10
k = 2*r - 1
    
for i in range(0, r): 
       
    for j in range(0, k): 
        print(end=' ') 
    k = k - 1
        # inner loop to handle number of columns  
    for j in range(0, i+1):   
        print("*", end="") 
       
    print()
