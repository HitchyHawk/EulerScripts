def main(r):
    spacing = 2
    a       = 1
    score   = 1
    counter = 0
    cr      = 2
    
    while cr <= r:
        a       += spacing
        score   += a
        counter += 1

        if counter  == 4:
            counter  = 0
            spacing += 2
            cr      += 1

    return score    
    
