
def countingValleys(steps, path):
    
    paths = list(path)
    sealevel = 0
    valley = 0
    
    for i in range(steps):
        if paths[i] == 'U':
            newsealevel = sealevel + 1
            if newsealevel < 0 and sealevel >= 0:
                valley+=1
            sealevel +=1
        if paths[i] == 'D':
            newsealevel = sealevel - 1
            if newsealevel < 0 and sealevel >= 0:
                valley+=1
            sealevel -=1
    return valley





