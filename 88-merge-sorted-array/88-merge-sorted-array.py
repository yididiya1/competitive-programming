class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l2 = len(nums2) - 1
        l1 = len(nums1) - n - 1
        pointer = len(nums1) - 1
        
        while pointer >= 0:
            # print(l1,l2,pointer)
            if l1 >= 0 and l2 >= 0:
                if nums2[l2] < nums1[l1]:
                    nums1[pointer] = nums1[l1]
                    l1 -= 1
                else:
                    nums1[pointer] = nums2[l2]
                    l2 -= 1
                pointer -= 1
            else:    
                break
                
        while l1 >= 0:
            nums1[pointer] = nums1[l1]
            pointer -= 1
            l1 -= 1
        
        while l2 >= 0:
            nums1[pointer] = nums2[l2]
            l2 -= 1
            pointer -= 1
        # print(l1,l2,pointer)