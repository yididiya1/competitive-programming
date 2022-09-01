class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        indegree = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        inBound = lambda row,col :  0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = deque()      
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                for r,c in dirs:
                    new_r = row+r
                    new_c = col+c
                    if inBound(new_r,new_c) and matrix[new_r][new_c] < matrix[row][col]:
                        indegree[row][col] += 1
                if indegree[row][col] == 0:
                    queue.append((row,col))

                    
        longest = 0
        while queue:
            for i in range(len(queue)):
                curr_r,curr_c = queue.popleft()
                for r,c in dirs:
                    new_r = curr_r+r
                    new_c = curr_c+c
                    if inBound(new_r,new_c) and matrix[new_r][new_c] > matrix[curr_r][curr_c]:
                        indegree[new_r][new_c] -= 1
                        if indegree[new_r][new_c] == 0:
                            queue.append((new_r,new_c))
            longest += 1
        
        return longest
                
        