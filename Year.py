def is_leap(year):
    leap = False
    
    # Write your logic here
    n = year%4
    m = year%400
    if (n==0) and (m%400==0 or year%100!=0):
        leap = True
    else:
        leap = False
    
    return leap

year = 2100
print(is_leap(year))