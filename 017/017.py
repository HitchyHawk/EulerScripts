def main(n):
    
    counter = 0
    for i in range(1,n):
        temp = ''
        a = str(i)
        if   len(a) == 3:
            temp = single(int(a[0]))+"hundredand"+ten(i-100*int(i/100))
        elif len(a) == 2:
            temp = ten(i)
        elif len(a) == 1:
            temp = single(i)
        print(temp)
        counter+=len(temp)
    return counter

## n[0]+hundred+and+n[1]ty+n[2]

def ten(n):
    if n >= 0 and n <10:
        return single(n)
    if n >= 10 and n < 20:
        if n == 10: return 'ten'
        elif n == 11: return 'eleven'
        elif n == 12: return 'twelve'
        elif n == 13: return 'thirteen'
        elif n == 14: return 'fourteen'
        elif n == 15: return 'fifteen'
        elif n == 16: return 'sixteen'
        elif n == 17: return 'seventeen'
        elif n == 18: return 'eighteen'
        elif n == 19: return 'nineteen'
    if n >= 20 and n < 30:  return 'twenty' +single(n-10*int(n/10))
    if n >= 30 and n < 40:  return 'thirty' +single(n-10*int(n/10))
    if n >= 40 and n < 50:  return 'forty'  +single(n-10*int(n/10))
    if n >= 50 and n < 60:  return 'fifty'  +single(n-10*int(n/10))
    if n >= 60 and n < 70:  return 'sixty'  +single(n-10*int(n/10))
    if n >= 70 and n < 80:  return 'seventy'+single(n-10*int(n/10))
    if n >= 80 and n < 90:  return 'eighty' +single(n-10*int(n/10))
    if n >= 90 and n < 100: return 'ninety' +single(n-10*int(n/10))

def single(n):
    if n == 0: return ''
    if n == 1: return 'one'
    if n == 2: return 'two'
    if n == 3: return 'three'
    if n == 4: return 'four'
    if n == 5: return 'five'
    if n == 6: return 'six'
    if n == 7: return 'seven'
    if n == 8: return 'eight'
    if n == 9: return 'nine'
