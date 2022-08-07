class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        @cache
        def isValid(index):
            if index == len(nums) :
                return True
            
            if index + 1 < len(nums) and nums[index] == nums[index+1] and isValid(index + 2):
                return True
            if index+2 < len(nums) and  nums[index] == nums[index+1] == nums[index+2] and isValid(index+3):
                return True
            if index+2 < len(nums) and nums[index]+1 == nums[index+1] == nums[index+2] - 1 and isValid(index+3):
                return True
            
            return False
        
        return isValid(0)