class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_stack = []
        _min = nums[0]
        
        for num in nums[1:]:
            while mono_stack and num >= mono_stack[-1][0]:
                mono_stack.pop()
            if mono_stack and mono_stack[-1][1] < num:
                return True
            
            mono_stack.append([num,_min])
            _min = min(_min,num)
            
        return False