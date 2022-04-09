class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        min_heap = []
        heapq.heapify(min_heap)
        
        
        
        for key in freq:
            heapq.heappush(min_heap,(freq[key],key))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return [val[1] for val in min_heap]
            
        
        
        
        
        
        