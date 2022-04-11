class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        neighbors = {i:[] for i in range(numCourses)}
        queue = deque()
        indegree = {i:0 for i in range(numCourses)}
        
        for start,dst in prerequisites:
            neighbors[start].append(dst)
            indegree[dst] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        top_sort  = []
        
        while queue:
            start = queue.popleft()    
            top_sort.append(start)
            for dst in neighbors[start]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)
        
        if len(top_sort) == numCourses:
            return top_sort[::-1]
        return []                
        
        
        