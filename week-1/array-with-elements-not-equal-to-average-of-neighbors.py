def rearrangeArray(nums):
        nums.sort()
        result = []
        
        left_index = 0
        right_index = len(nums) -1
        
        
        while len(result) != len(nums):
            result.append(nums[left_index])
            left_index += 1
            
            if left_index <= right_index:
                result.append(nums[right_index])
                right_index -= 1
            
        return result

example = rearrangeArray([6,2,3,4,5,1])
print(example)
            