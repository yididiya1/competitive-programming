class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        
        seen = {}
        ans = float('inf')
        
        for i in range(len(cards)):
            if cards[i] in seen:
                ans = min(ans,(i-seen[cards[i]]))
            seen[cards[i]] = i
        
        if ans != float('inf') :
            return ans+1
        return -1
            
        
        
        