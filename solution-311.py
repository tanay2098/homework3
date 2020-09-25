#initializing the following variables to store the values.
gallons_used=0
miles=0
miles_per_gallon=0
total_gallons=0
total_miles=0
total_mpg=0

gallons_used=float(input('Enter the gallons used (-1 to end): '))#taking user input for gallons
while(gallons_used==0 or gallons_used<=-2):#Loop to check and validate user input
    gallons_used=float(input('Please enter a valid value: '))

if(gallons_used!=-1):
    miles=float(input('Enter the miles driven: '))#taking user input for miles
while(miles<=0):#Loop to check and validate user input
    miles=float(input('Please enter a valid value: '))

while(gallons_used!=-1):

    miles_per_gallon=miles/gallons_used#Calculating miles per gallon
    print('The miles/gallon for this tank was: ',+miles/gallons_used)
    total_gallons+=gallons_used#Adding the gallon used after each iteration
    total_miles+=miles#Adding the miles used after each iteration
    

    gallons_used=float(input('Enter the gallons used (-1 to end): '))#taking user input for gallons
    while(gallons_used==0 or gallons_used<=-2):#Loop to check and validate user input
        gallons_used=float(input('Please enter a valid value: '))
    if(gallons_used!=-1):

        miles=float(input("Enter the miles driven: "))#taking user input for miles
    else:
        avg=total_miles/total_gallons#Calculating the total average
        print('The overall average miles/gallon was: ',+ avg)
    