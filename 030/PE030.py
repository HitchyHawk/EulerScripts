def main(r):
    for i in range(2,r):
        if powers(i,5) == i:
            print(i)


def powers(i,p):
    count = 0
    I = str(i)
    for a in range(len(I)):
        count += int(I[a])**p

    return count
        
