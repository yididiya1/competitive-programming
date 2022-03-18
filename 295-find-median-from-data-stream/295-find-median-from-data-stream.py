class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.maxHeap,-1*num)
        
        
        if self.minHeap and self.maxHeap:
            if -1*self.maxHeap[0] > self.minHeap[0]:
                removed = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap,-1*removed)
            
        if len(self.maxHeap) - len(self.minHeap) > 1:
            removed = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap,-1*removed)
            
        if len(self.minHeap) - len(self.maxHeap) > 1:
            removed = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-1*removed)
            
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return ((-1*self.maxHeap[0])+(self.minHeap[0]))/2
        elif len(self.minHeap) > len(self.maxHeap):
            return (self.minHeap[0])
        else:
            return (-1*self.maxHeap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()