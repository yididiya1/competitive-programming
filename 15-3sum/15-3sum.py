class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        def two_sum(numss,target):
            l = 0
            r = len(numss) - 1
            
            answers = []
            
            while l < r:
                if numss[l] + numss[r] == target :
                    answers.append([numss[l],numss[r]])
                    while r-1 > l and numss[r-1] == numss[r]:
                        r -= 1
                    while l + 1 < r and numss[l+1] == numss[l]:
                        l += 1  
                    r -= 1
                    l += 1
                    
                elif numss[l] + numss[r] > target :
                    r -= 1
                else:
                    l += 1
                    
            return answers
        
        
        output = []
        
        i = 0
        
        
        while i < len(nums):
            target = 0 - nums[i]
            check = two_sum(nums[i+1:],target)
            # print(check,i)
            if check :
                for z in check:
                    output.append([nums[i],z[0],z[1]])
                
                while i + 1< len(nums) and  nums[i] == nums[i+1]:
                    i += 1
            
            i += 1
            
        return output    
            
        
        
        
        
        