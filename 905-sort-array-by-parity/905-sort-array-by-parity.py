class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        current = 0
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                # print(current,i)
                nums[i],nums[current] = nums[current],nums[i]
                current += 1
                
        return nums
        