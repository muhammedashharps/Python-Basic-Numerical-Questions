# Checking a Leap year 

year = int(input("Enter a Year  :"))

if (year%4==0 and year%100 !=0) or (year%400 == 0):
    print("Leap Year")
else:
    print("No Leap Year")
    
# Condition To Check whether a year is leap year or not 
# 1. Should be divisible by 4 but not with 100 at any cost (#Mandatory) 
#2. Can also be divisible with 400 (#Not Mandtaroy)