class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0 for i in range(len(nums2)+1)] for j in range(len(nums1)+1)]
        
        
        for row in range(len(nums1)-1,-1,-1):
            for col in range(len(nums2)-1,-1,-1):
                if nums1[row] == nums2[col]:
                    dp[row][col] = dp[row+1][col+1] + 1 
                            
        return max(max(row) for row in dp)