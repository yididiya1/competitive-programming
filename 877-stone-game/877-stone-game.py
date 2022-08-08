class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        self.alice = 0
        
        @cache
        def dp(l,r):
            # print(l,r)
            if r - l == 1:
                return abs(piles[l]-piles[r])
        
            take_left = piles[l] - dp(l+1,r)
            take_right = piles[r] - dp(l,r-1)
            
            # print(max(take_left,take_right))
            return max(take_left,take_right)
            
        
        alice = dp(0,len(piles)-1)
        
        if alice > 0:
            return True
        return False
            
        