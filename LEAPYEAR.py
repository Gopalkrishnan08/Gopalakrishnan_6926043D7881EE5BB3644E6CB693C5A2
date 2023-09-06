input_year = int(input("Enter the Year to be checked: "))
if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
    print("%d is Leap Year" %input_year)
else:
    print("%d is Not the Leap Year" %input_year)