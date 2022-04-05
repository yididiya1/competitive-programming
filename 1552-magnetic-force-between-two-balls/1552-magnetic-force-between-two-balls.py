class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        start = 1
        end = position[-1] - position[0]
        answer = float('-inf')
        
        def getDif(force):         
            left = m-1
            l = position[-1]
            current = position[0]
  
            for i in range(1,len(position)):
                if position[i] - current >= force:
                    # print("===>",i,current,left)
                    left -= 1
                    current = position[i]

            if left > 0:
                return False
            return True
            

        while start <= end :
            mid = (start+end)//2
            result = getDif(mid)
            
            if result == True:
                answer = max(answer,mid)
                start = mid+1
            else:
                end = mid - 1
        

        return answer
    
                
        
            
        