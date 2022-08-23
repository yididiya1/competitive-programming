class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        self.bound = lambda row,col: 0 <= row < len(mat) and 0 <= col < len(mat[0])        
        def getDiagonal(row,col):
            ans = []
            r = row
            c = col
            while self.bound(r,c):
                ans.append(mat[r][c])
                r,c = r+1,c-1
            
            return ans
        forward = True
        for i in range(len(mat[0])):
            answer = getDiagonal(0,i)
            if forward:
                result.extend(answer[::-1])
                forward = not forward
            else:
                result.extend(answer)
                forward = not forward
        
        col = len(mat[0]) - 1
        for i in range(1,len(mat)):
            answer = getDiagonal(i,col)
            if forward:
                result.extend(answer[::-1])
                forward = not forward
            else:
                result.extend(answer)
                forward = not forward
                
        return result
            
        
        