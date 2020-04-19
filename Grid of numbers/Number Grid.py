def start(name):
    steps = 4
    ttLines = lineCount(name)
    x = ttLines

    ##Creates the grid
    grid = [0]*x
    
    for i in range(x):
        grid[i] = [0]*x


    ##Opens the text
    file = open(name, 'r')
    
    ##Collects the data and puts into grid
    for r in range(ttLines):
        
        ##reads the rows
        for c in range(ttLines):
            ##puts into 
            grid[r][c] = int(convert(file.readline(2)))

            ##Skips Space
            file.readline(1)
    file.close()

    
    ##Checking Phase
    buffer = 1
    final = 1
    
    ##Checks all horizontals
    for r in range(x):
        for c in range(x-steps+1):
            for position in range(c,c+steps):
                buffer *= grid[r][position]

            ##replaces the smaller result with bigger result
            if buffer > final:
                final = buffer
            buffer = 1

    ##Checks all Verticals
    for c in range(x):
        for r in range(x-steps+1):
            for position in range(r,r+steps):
                buffer*=grid[position][c]
            
            ##replaces the smaller result with bigger result
            if buffer > final:
                final = buffer
            buffer = 1

    ##first Diagonals from top left to bottom right
    for r in range(x-steps+1):
        for c in range(x-steps+1):
            for position in range(c,c+steps):
                try:
                    buffer*= grid[r+position][position]
                except IndexError: buffer *= 0
                
            if buffer > final:
                final = buffer
            buffer = 1
            
    ##Second Diagonals from bottom left to top right
    for r in range(steps-1,x):
        for c in range(x-steps+1):
            for position in range(c,c+steps):
                try:
                    buffer*=grid[r-position][position]
                except IndexError: buffer *= 0
                
            if buffer > final:
                final = buffer
            buffer = 1
    print(final)

            

def lineCount(name):
    file = open(name, 'r')
    n = '~'
    count = 0
    while n != '':
        n = file.readline()
        count+= 1

    file.close()
    return count-1

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
        
    
    
