class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
 
        freq = defaultdict(int)
        total = 0
        
        for t in time:
            if t%60 == 0 : total += freq[0]
            else : total += freq[60 - (t%60)]
            freq[t%60] += 1
            
        return total
                
        