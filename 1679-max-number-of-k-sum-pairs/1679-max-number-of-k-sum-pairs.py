class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        freq = Counter(nums)
        count = 0
        
        for num in nums:
            if k - num in freq:
                if k - num == num:
                    if freq[num] > 1:
                        freq[k-num] -= 2
                        count += 1
                else:
                    if freq[num] and freq[k-num] > 0:
                        freq[k-num] -= 1
                        freq[num] -= 1
                        count += 1
            # print(count)
            
        return count
        
        
        
        
        
        