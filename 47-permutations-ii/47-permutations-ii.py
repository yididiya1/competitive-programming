class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         perm = []
#         freq = Counter(nums)
        
#         def backtrack():
#             if len(perm) == len(nums):
#                 res.append(perm.copy())
                
#             for n in freq:
#                 if freq[n] > 0:
#                     perm.append(n)
#                     freq[n] -= 1
#                     backtrack()
#                     freq[n] += 1
#                     perm.pop()
                
#         backtrack()
#         return res


        output = []
        freq = Counter(nums)
        
        def backtrack(curr):
            if len(curr) == len(nums):
                # print(curr)
                output.append(curr.copy())
            
            if len(curr) > len(nums):
                return
            
            for n in freq:
                if freq[n] > 0:
                    curr.append(n)
                    freq[n] -= 1
                    backtrack(curr)
                    freq[n] += 1
                    curr.pop()
                    
        backtrack([])
        return output