def main(a):
    DOW = 1
    D = 1
    DOM = 1
    count = 0
    y = 1900
    m = 1
    while D <= a:
        D   += 1
        DOM += 1
        DOW += 1

        if m == 1 or m == 4 or m == 6 or m == 11 and DOM == 31:
            m += 1
            DOM = 1

        if m == 3 or m == 5 or m == 7 or m == 8 or m == 9 or m == 10 and DOM == 32:
            m += 1
            DOM = 1
            
        if m == 2 and y%4 == 0 and y%400 != 0 and DOM == 30:
            m += 1
            DOM == 1
            
        elif m == 2 and DOM == 29:
            m += 1
            DOM = 1
            

        if m == 12 and DOM == 32:
            y += 1
            m = 1
            DOM = 1
            
            
        
        
        if DOW == 7 and DOM == 1:
            print(y, m)
            count += 1
        
        if DOW == 8:
            DOW = 1

            
    return count
##Jan 30
##feb 28 + 1 every four years
##mar 31
##apr 30
##may 31
##jun 30
##jul 31
##aug 31
##sep 31
##oct 31
##nov 30
##dec 31
