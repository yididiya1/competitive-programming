class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        answer = []
        
        
        for col in range(c):
            new_row = []
            for row in range(r):
                new_row.append(matrix[row][col])
            answer.append(new_row)
            
        return answer
        
        