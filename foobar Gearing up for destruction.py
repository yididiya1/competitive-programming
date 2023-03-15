from fractions import Fraction

def solution(pegs):
    # Your code here
    def checkfinal(radius):
        last = -1
        nextR = radius - temp
        if (temp < 1 or nextR < 1):
            return -1
        else:
            return nextR

    minDiff = float('inf')
    is_even = len(pegs)%2 == 0
    total = (-pegs[0] + pegs[-1]) if is_even  else (-pegs[0] - pegs[-1])
    
    for i in range(1,len(pegs)-1):
        minDiff = min((pegs[i+1] - pegs[i]),minDiff)
        total += 2 * ((-1)**(i+1)) * pegs[i]
    
    possible =  Fraction(2 * (float(total)/3 if is_even else total)).limit_denominator()
    
    if possible < 2: return [-1,-1]
    temp = possible
    for i in range(0,len(pegs)-1):
        newR =  pegs[i+1] - pegs[i]
        x = checkfinal(newR)
        if x == -1:
            return [-1,-1]
        temp = x
            
    return [possible.numerator, possible.denominator]
    
print(solution([4, 17, 50]))
