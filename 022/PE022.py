import os
def main():
    name = 'n.txt'
    fileName = open(name,'r')

    raw = fileName.read()
    raw = raw.replace('"', "")
    raw = raw.lower()
    raw = raw.split(',')
    raw.sort()
 
    final = 0
    for i in range(len(raw)):
        final += Score01(raw[i])*(i+1)

    fileName.close()
    return final


def Score01(name):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    score = 0
    for i in range(len(name)):
            score += alpha.index(name[i])+1
    return score
        
    
    

    
