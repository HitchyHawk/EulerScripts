import time
import os

def flips(name):
    temp = open('temp','w')
    l = lineChecker(name)
    w = 'buffer usefull letter'
    for i in range(l):
        file = open(name,'r')
        for i in range(l-1):
            w = file.readline()
        w = file.readline()
        temp.write(w)
        file.close()
        l-=1
    temp.close()
    os.rename('temp',"f_"+name)

def base(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a>=b: return(a+c)
    else: return (b+c)

def lineChecker(name):
    line = '~'
    runningTotal = 0
    file = open(name, 'r')
    while line != '':
        runningTotal+= 1
        line = file.readline()
    return runningTotal

def convert(a):
    if a == '01':
        return 1
    elif a == '02':
        return 2
    elif a == '03':
        return 3
    elif a == '04':
        return 4
    elif a == '05':
        return 5
    elif a == '06':
        return 6
    elif a == '07':
        return 7
    elif a == '08':
        return 8
    elif a == '09':
        return 9
    else: return a

def triangle(name):
    t =time.time()
    flips(name)
    first = open("f_"+name,'r')
    second = open("f_"+name, 'r')
    flip = 0
    
    lines = lineChecker("f_"+name)
    buffer = [0]*(lines-1)
    second.readline()
    c = '~'
    ##Do this for one less then amount of lines
    while c != '':
        if flip == 0:
            b = convert(first.readline(2))
            first.readline(1)
        steps = 0

        ##Do this for one less then amount of lines
        ##Reads first row and second then calculates
        ##Then puts the outputs into the list
        
        for i in range(0,lines-2):
            if flip == 0:
                ##For the first read
                a = b
                b = convert(first.readline(2))
            else:
                ##For when switching to lists
                a = buffer[i]
                b = buffer[i+1]
            
            c = convert(second.readline(2))
            
            if c != '':
                buffer[i] = base(a,b,c)

            ##Avoiding spaces
            c = second.readline(1)
            if flip == 0:
                first.readline(1)

        flip = 1
        first.close()
        lines -= 1
        if lines == 1:
            print(buffer[0])
            second.close()
            print(format(time.time()-t,'.2f'))
            os.remove("f_"+name)
            return
    
    









    


    
    
