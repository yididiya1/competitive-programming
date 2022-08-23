class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral = []
        
        
        
        
        def getSpiral(r1,r2,c1,c2):
            # print(r1,r2,c1,c2)
            visited = set()
            for i in range(c1,c2+1):
                # print("Right")
                if (r1,i) not in visited:
                    spiral.append((r1,i))
                    visited.add((r1,i))
            for i in range(r1,r2+1):
                # print("Down")
                if (i,c2) not in visited:
                    spiral.append((i,c2))
                    visited.add((i,c2))
            for i in range(c2,c1,-1):
                # print("Left")
                if (r2,i) not in visited:
                    spiral.append((r2,i))
                    visited.add((r2,i))
            for i in range(r2,r1,-1):
                # print("Up")
                if (i,c1) not in visited:
                    spiral.append((i,c1))
                    visited.add((i,c1))
            
            
            
        row1,row2 = 0 ,len(matrix) - 1
        col1,col2 = 0 , len(matrix[0]) - 1
        total = len(matrix)*len(matrix[0])
        while len(spiral)<total:
            # print(spiral)
            getSpiral(row1,row2,col1,col2)
            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1
        
        spiral = [matrix[x][y] for x,y in spiral]
        return spiral    