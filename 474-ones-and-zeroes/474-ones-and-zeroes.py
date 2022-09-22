class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        
        count = [[st.count('0'),st.count('1')] for st in strs]

       
        @cache
        def dp(index,one,zero):
            if index >= len(strs):
                return 0
            
            take_me = 0 if one-count[index][1] < 0 or zero - count[index][0] < 0 else 1 + dp(index+1,one-count[index][1],zero-count[index][0])
            skip_me = dp(index+1,one,zero)
            
            return max(take_me,skip_me)
        
        
        return dp(0,n,m)