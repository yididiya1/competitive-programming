def smallerNumbersThanCurrent(nums):
        
        count = [0]*len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j] > nums[i]:
                    count[j] += 1
                    
        return count

test = smallerNumbersThanCurrent([8,1,2,2,3])
print(test)