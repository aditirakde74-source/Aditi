day=int(input("enter the day:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
if month<1 and month>12:
    print("invaliddate")
else:
    if month==2:
        if month % 400==0 or month % 4==0 and month%100!=0:
         maxdays=29
        else:
         maxdays=28
    elif month==4 or month==6 or month==9 or month==11:
        maxdays=30
    else:
        maxdays=31
        
if day>=1 and day<=maxdays:
 print("invaliddate")
else:
   print("validdate")
