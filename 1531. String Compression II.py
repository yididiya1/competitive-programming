class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        
        @cache
        def dp(index, curr_char, count, left):
            
            if index == len(s):
                return 0
            
            delete_distance = float('inf')
            
            if left > 0:
                delete_distance = dp(index+1, curr_char, count, left - 1)
            
            curr_letter = s[index]
            
            keep_cost = float('inf')
            if curr_letter == curr_char:
                add = 0
                if count == 1 or len(str(count + 1)) > len(str(count)):
                    add = 1
                
                keep_cost = add + dp(index+1, curr_letter, count + 1, left)
            else:
                
                keep_cost = 1 + dp(index+1, curr_letter, 1, left)
            
            return min(keep_cost, delete_distance)
                
            
        res = dp(0, "", 0, k)
        return res
