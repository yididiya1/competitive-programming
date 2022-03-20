class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums) 
        pairs = [(num, count) for num, count in freq.items()] 
        pairs.sort() 
        used, not_used = 0, 0 
        for i, (num, count) in enumerate(pairs): 
            if i == 0 or pairs[i - 1][0] != num - 1:
                # no previous noum or not num - 1 
                not_used = max(used, not_used) # choose max 
                used = num * count + not_used # add point from this num 
            else: 
                used, not_used = num * count + not_used, max(used, not_used) 
        return max(used, not_used)
        
        