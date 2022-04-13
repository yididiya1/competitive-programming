class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict()
        count = 0
        
        freq[0] = 1
        
        nums.insert(0,0)
        
        for i in range(1,len(nums)):
            temp = nums[i-1] + 1 if nums[i]%2 != 0 else nums[i-1] 
            nums[i] = temp
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            
            if nums[i] - k in freq:
                count += freq[nums[i] - k]
                

        return count
            
            
            
            
            