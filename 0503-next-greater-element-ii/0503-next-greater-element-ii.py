class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        
        
        greater = [-1 for i in range(n)]
        
        mono_stack = []
        count = 0
        i = 0
        
        while i < len(nums):
            if not mono_stack:
                mono_stack.append(i)
                i += 1
            else:
                while mono_stack and nums[mono_stack[-1]] < nums[i]:
                    x = mono_stack.pop()
                    if x < len(greater):
                        greater[x] = nums[i]
                
                mono_stack.append(i)
                i += 1
                
        return greater
        
        
        
        
        
        
        