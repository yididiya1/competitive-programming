class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0     
        while maxHeap or q:
            time += 1
           
            if maxHeap:
                curr = 1 + heapq.heappop(maxHeap)
                if curr:
                    q.append([curr,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
                
        return time
                
        
        