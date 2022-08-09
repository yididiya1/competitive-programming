class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        # print(arr)
        def getTwo(nums,target):
            l  = 0
            r = len(nums) - 1
            ans  = set()
        
        
            while l <= r:
                if nums[l] * nums[r] == target:
                    ans.add((l,r))
                    ans.add((r,l))
                    l += 1
                    r -= 1
                elif nums[l]*nums[r] > target:
                    r -= 1
                else:
                    l += 1
                    
            ans = list(ans)
            return ans
        
        
        
        freq  = {}
        
        @cache
        def dp(index):
            x = getTwo(arr,arr[index])
            # print(index,x)
            if not x:
                return 0
            else:
                mine = 0
                for l,r in x:
                    mine += 1
                    mine += dp(l) * dp(r)
                    mine += dp(l)
                    mine += dp(r)
                return mine
        
        total = 0
        for i in range(len(arr)):
            x = dp(i)
            # print(i,x)
            total += x
        
        return (total+len(arr))%(10**9 + 7)
        # print(dp(3))
        
                    
            
        
        
        