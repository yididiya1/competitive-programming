class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        output = []
        
        prev = float('-inf')
        
        for i in range(len(nums)-1):
            if nums[i] == prev:
                continue
            target = 0 - nums[i]
            # print(i,target)
            l = i+1
            r = len(nums) - 1
            prevl = float('-inf')
            prevr = float('-inf')
            
            while l < r:
                if nums[l] + nums[r] == target:
                    if prevl != nums[l] and prevr != nums[r]:
                        output.append([nums[i],nums[l],nums[r]])
                        prevl = nums[l]
                        prevr = nums[r]
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            
            # print(res,"=====")
            prev = nums[i]
                
        
        return output
        