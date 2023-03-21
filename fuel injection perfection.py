

def solution(n):
    n = int(n)
    count = 0
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        elif n == 3 or ((n >> 1) & 1 == 0):
            n -= 1
        else:
            n += 1
        count += 1
    return count
    
print(solution("12354678657432456786543256434567654317"))
