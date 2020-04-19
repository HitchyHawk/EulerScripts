import time
def main(m):
    t= time.time()
    temp = []
    for a in range(2,m+1):
        for b in range(2,m+1):
            temp.append(a**b)

    temp.sort()
    final = []
    
    for i in range(0,len(temp)):
        if temp[i] not in final:
            print(temp[i])
            final.append(temp[i])
        
    print(len(final),'\nTime:',format(time.time()-t,'.2f'))
            
