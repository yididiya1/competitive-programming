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
        
        
        
        
        
        memo = {}
        
        def dp(index):
            if index in memo:
                return memo[index]
            x = getTwo(arr,arr[index])
            if not x:
                return 0
                memo[index] = 0
            else:
                mine = 0
                for l,r in x:
                    mine += 1
                    mine += dp(l) * dp(r)
                    mine += dp(l)
                    mine += dp(r)
                memo[index] = mine
                return mine
        
        total = 0
        for i in range(len(arr)):
            x = dp(i)
            total += x
        
        return (total+len(arr))%(10**9 + 7)
        
        
                    
            
        
        
        