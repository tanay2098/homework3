a=0#initializing variable for storing quarter
b=0#initializing variable for storing dime
c=0#initializing variable for storing nickle
d=0#initializing variable for storing penny
dollar=100#Taking constant value of one dollar in the form of cents
purchase_amt=int(input('Enter a price in cents: '))#Taking purchase price from user in cents.
change=dollar-purchase_amt#Calculating the change and storing it in variable

if purchase_amt==dollar:
    print('No change due')
else:
    print('Your Change is:')

if change>=25:#Calculating Quarters
    a=(change//25)
    change=change%25
    print(a,'quarters')

if change>=10:#Calculating Dimes
    b=(change//10)
    change=change%10
    print(b,'dimes')

if change>=5:#Calculating Nickles
    c=(change//5)
    change=change%5
    print(c,'nickles')

if change>0:#Calculating Pennies
    d=(change//1)
    change=0
    print(d,'pennies')

