class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        if not tokens:
            return 0
        
        tokens.sort()
        
        l = 0
        r = len(tokens) - 1
        score = 0
        
        while l < r:
            if tokens[l] <= power:
                power -= tokens[l] 
                score += 1
                l += 1
            else:
                if tokens[l] <= power+tokens[r] and score > 0:
                    power += tokens[r]
                    score -= 1
                    r -= 1
                else:
                    return score
        
        # print(score,tokens[l],power)
        if tokens[l] <= power:
            score += 1
        
        return score          
            
           
            
        