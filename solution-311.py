gallons_used=0
miles=0
miles_per_gallon=0
total_gallons=0
total_miles=0
total_mpg=0


gallons_used=float(input('Enter the gallons used (-1 to end): '))

if(gallons_used!=-1):
    miles=float(input("Enter the miles driven: "))

while(gallons_used!=-1):

    miles_per_gallon=miles/gallons_used
    print('The miles/gallon for this tank was: ',+miles/gallons_used)
    total_gallons+=gallons_used
    total_miles+=miles
    

    gallons_used=float(input('Enter the gallons used (-1 to end): '))
    if(gallons_used!=-1):

        miles=float(input("Enter the miles driven: "))
    else:
        avg=total_miles/total_gallons
        print('The overall average miles/gallon was: ',+ avg)
    