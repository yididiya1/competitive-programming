class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        steps = 0
        binary = bin(num)[2:]
        
        for b in binary:
            if b == "1":
                steps += 2
            else:
                steps += 1
                
        return steps-1
        