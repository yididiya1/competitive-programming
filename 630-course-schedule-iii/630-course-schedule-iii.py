class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        heapq.heapify(pq)
        courses.sort(key = lambda x : x[1])
        day = 0
        
        for course in courses:
            if day+course[0] <= course[1]:
                day += course[0]
                heapq.heappush(pq,-course[0])
            elif pq and abs(pq[0]) > course[0]:
                d = heapq.heappop(pq)
                day += course[0] - abs(d)
                heapq.heappush(pq,-course[0])
                
        return len(pq)
        
        
        
        