class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num%2 == 0 : even_sum += num
        ans = []
        
        for val,idx in queries:
            if nums[idx]%2 == 0:
                if (nums[idx]+val)%2 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[idx]
                ans.append(even_sum)
                nums[idx] += val
            else:
                if (nums[idx]+val)%2 == 0:
                    even_sum += (nums[idx]+val)
                ans.append(even_sum)
                nums[idx] += val
                
                
        return ans