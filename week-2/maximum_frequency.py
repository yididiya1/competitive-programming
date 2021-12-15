def maxFrequency(self, nums, k):
        frequency = 1
        nums.sort()
        while k > 0:
            for i in range(len(nums)-1):
                diff = nums[i+1] - nums[i]
                if diff > 0 and diff <= k and k > 0 :
                    nums[i] += diff
                    k -= diff              
                elif diff > k:
                    k -= 1
        
        print(nums)

        for i in range(len(nums)):
            if nums.count(nums[i])> frequency:
                frequency = nums.count(nums[i])
         

        return frequency
                