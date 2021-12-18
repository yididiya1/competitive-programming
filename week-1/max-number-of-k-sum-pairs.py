def maxOperations(nums,k):
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        
        while i < j :
            if nums[i] + nums[j] < k:
                i+= 1
            elif nums[i] + nums[j] > k:
                j-=1
            else:
                i+=1
                j-=1
                count += 1
                
        return count

example = maxOperations([3,1,5,1,1,1,1,1,2,2,3,2,2],1) 
print(example)  