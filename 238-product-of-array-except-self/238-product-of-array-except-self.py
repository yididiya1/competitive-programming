class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_left = [nums[0]]
        
        
        
        for i in range(1,len(nums)):
            prefix_product_left.append(nums[i] * prefix_product_left[i-1]) 
            
        for i in range(len(nums)-2,-1,-1):
            nums[i] *= nums[i+1]
        
        
        prefix_product_left.insert(0,1)
        nums.insert(0,1)
        nums.append(1)
        
        # print(prefix_product_left)
        # print(nums)
        
        
        for i in range(1,len(prefix_product_left)):
            nums[i] = prefix_product_left[i-1] * nums[i+1]
            
        return nums[1:len(nums)-1]
        
        