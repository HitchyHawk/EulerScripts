def isPrime(a):
    if a == 2 or a == 3 or a == 5 or a ==7:
        return True
    elif a%2 == 0:
        return False
    b = a**0.5
    c = 3
    while c <= b:
        if a%c == 0:
            return False
        c+= 2
    return True

def quad(n,a,b):
    return (n**2)+a*n+b

def main(r):
    best  = 0
    for a in range(-r,r):
        for b in range(-r,r):
            n     = 0
            count = 0
            while isPrime(abs(quad(n,a,b)))== True:
                count += 1
                n     += 1

            if count>best:
                best  = count
                bestA = a
                bestB = b
    return best, bestA, bestB


            

    
