class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        
        for i in range(len(nums1)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        
        result = []
        while heap and k > 0:
            cur_sum,i,j = heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])
            if j+1 < len(nums2):
                heapq.heappush(heap,((nums1[i]+nums2[j+1]),i,j+1))
            k-= 1
        
        return result