def is_leap(year):
    leap = True
    
    # Write your logic here
    
    if  year % 4 == 0 or year % 400==0:
        
        return leap
        
    else:
        return False
    
year = int(input("Enter year to check whether its a leap year:" ))
print(is_leap(year))