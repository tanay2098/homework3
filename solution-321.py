a=0
b=0
c=0
d=0
dollar=100
user_amt=int(input('Enter a price in cents: '))
change=dollar-user_amt

if user_amt==dollar:
    print('No change due')
else:
    print('Your Change is:')

if change>=25:
    a=(change//25)
    change=change%25
    print(a,'quarters')

if change>=10:
    b=(change//10)
    change=change%10
    print(b,'dimes')

if change>=5:
    c=(change//5)
    change=change%5
    print(c,'nickles')

if change>0:
    d=(change//1)
    change=0
    print(d,'pennies')

