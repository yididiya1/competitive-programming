class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        maxHeap = []
        heapq.heapify(maxHeap)
        
        
        for i in range(len(nums)):
            # print(maxHeap,"==")
            if not maxHeap:
                heapq.heappush(maxHeap,(nums[i],1))
                # maxHeap.append((1,1))
            else:
                while maxHeap and maxHeap[0][0]+1 < nums[i]:
                    ee,ll = heapq.heappop(maxHeap)
                    if ll  < 3:
                        return False
                if maxHeap:
                    end,length = maxHeap[0]
                    if end == nums[i]:
                        heapq.heappush(maxHeap,(nums[i],1))
                    else:
                        e,l = heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap,(nums[i],l+1))
                else:
                    heapq.heappush(maxHeap,(nums[i],1))
                
                    
        # print(maxHeap)       
        
        while maxHeap:
            e,l = heapq.heappop(maxHeap)
            if l < 3:
                return False
            
        return True
            
                
        
        