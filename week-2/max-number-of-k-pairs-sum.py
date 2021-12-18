#not finished yet
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_copy = nums.copy()
        no_of_ops = 0
        
        for i in range(1,len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 :
                print(key,nums[j],key+nums[j])
                if key+nums[j] == 5 :
                   # print(nums_copy)
                   # print(key,nums[j],key+nums[j])
                    if key in nums_copy and nums[j] in nums_copy:
                        nums_copy.remove(key)
                        nums_copy.remove(nums[j])
                        no_of_ops += 1
                nums[j+1] = nums[j]                
                j-=1
           
            nums[j+1] = key
        
        print(nums_copy,no_of_ops)
        return no_of_ops
        