class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        
        self.left,self.right = 0 , len(mat) - 1
        
        def rotate():
            
            
            while self.left < self.right:
                top,bottom = self.left,self.right
                for i in range(self.right-self.left):
                    topleft = mat[top][self.left+i]
                    
                    mat[top][self.left+i] = mat[bottom-i][self.left]
                    mat[bottom-i][self.left] = mat[bottom][self.right-i]
                    mat[bottom][self.right-i] = mat[top+i][self.right]
                    mat[top+i][self.right] = topleft
                
                self.left += 1
                self.right -= 1
        
        
        
        
        for i in range(4):
            if mat == target:
                return True
            rotate()
            self.left , self.right = 0 ,len(mat) - 1
            # print(mat)
            
            
            
            
        return False
        