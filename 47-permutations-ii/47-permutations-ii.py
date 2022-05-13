class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        freq = Counter(nums)
        
        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                
            for n in freq:
                if freq[n] > 0:
                    perm.append(n)
                    freq[n] -= 1
                    backtrack()
                    freq[n] += 1
                    perm.pop()
                
        backtrack()
        return res