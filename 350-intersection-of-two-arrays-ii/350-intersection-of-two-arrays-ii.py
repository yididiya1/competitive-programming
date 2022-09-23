class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        l1 = 0
        l2 = 0
        
        while l2 < len(nums2) and l1 < len(nums1):
            if nums2[l2] == nums1[l1]:
                result.append(nums1[l1])
                l1 += 1
                l2 += 1          
            elif nums2[l2] > nums1[l1]:
                l1 += 1
            else:
                l2 += 1
                
        return result
        