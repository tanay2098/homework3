print('(a)')

for row in range(0,10):#Loop for Rows

    for column in range(0,row+1):#Loop for Column

        print("*",end='')#Printing aestrik
    print('')#new line


print('\n(b)')

for row in range(10,0,-1):#Loop for Column

    for column in range(0,row):#Loop for row

        print("*",end='')#Printing Aestrik
    print('')#new line

print('\n(c)')

row=1#initializing variable for row
while(row<=10):#Loop for rows
    col=1#initializing variable for column
    while(col<=10):#Loop for columns
        if(col<row):#Condition for printing
            print(' ',end='')# Printing Space
        else:
            print('*',end='')#Printing *
        col+=1#Incrementing Column by 1 after each iteration
    row+=1##Incrementing row by 1 after each iteration
    print('')#new line

print('\n(d)')

r=10#Initializing variable for row
k = 2*r - 1# Variable for Spacing
    
for i in range(0, r): #Loop for rows
       
    for j in range(0, k):#Loop for spacing
        print(end=' ') 
    k = k - 1#Decrementing space variable after each iteration
          
    for j in range(0, i+1):# loop for columns   
        print("*", end="") 
       
    print()#new line
