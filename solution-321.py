a=0
b=0
c=0
d=0
amt=int(input('Enter a price of one dollar or less: '))

if amt>=25:
    a=amt/25
    amt=amt%25

if amt>=10:
    b=amt/10
    amt=amt%10

if amt>=5:
    c=amt/5
    amt=amt%5

if amt>0:
    d=amt/1
    amt=0

print('Your Change is: \n',a, 'quarters\n',b, 'dimes\n',c, 'nickles\n',d, 'pennies') 

