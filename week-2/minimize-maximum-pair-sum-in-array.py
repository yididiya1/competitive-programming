def minPairSum(nums):
        nums.sort()
        maxpairsum = 0
        i = 0
        j = len(nums) - 1
        while i < j :
            if (nums[i]+nums[j]) > maxpairsum:
                maxpairsum = nums[i]+nums[j]
            i+=1
            j-=1
        
        return maxpairsum

example = minPairSum([3,5,2,3])
print(example)