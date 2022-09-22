class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        
        count = []
        for st in strs:
            x = st.count('0')
            y = st.count('1')
            count.append([x,y])
        
        # print(count)
        
        @cache
        def dp(index,one,zero):
            if index >= len(strs):
                return 0
            
            # if one-count[index][1] < 0 or zero - count[index][0] < 0:
            #     print("Here",index,one,zero)
            #     return 0
            
            take_me = 0 if one-count[index][1] < 0 or zero - count[index][0] < 0 else 1 + dp(index+1,one-count[index][1],zero-count[index][0])
            skip_me = dp(index+1,one,zero)
            
            # print(index,max(take_me,skip_me),zero,one)
            return max(take_me,skip_me)
        
        
        return dp(0,n,m)