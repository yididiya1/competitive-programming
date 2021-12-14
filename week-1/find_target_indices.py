def targetIndices(nums, target):
        indexes = []
        for i in range(1,len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1           
            nums[j+1] = key
         
        for i in range(len(nums)):
            if nums[i] == target:
                indexes.append(i)
                
        return indexes

example = targetIndices([1,2,5,2,3],2)
print(example)
            