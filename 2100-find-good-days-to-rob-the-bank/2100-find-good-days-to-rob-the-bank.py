class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        non_increasing = [0]
        non_decreasing = [0]
        
        

        output = []
        
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                non_increasing.append(non_increasing[i-1]+1)
            else:
                non_increasing.append(0)
                
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                non_decreasing.append(non_decreasing[-1]+1)
            else:
                non_decreasing.append(0)
        
        
        
        
        non_decreasing.reverse()
        
        # end = len(security) - time   if time > 0 else len(security)-1
        # start = time if time > 0 else 1
        
        
        # print(non_increasing)
        # print(non_decreasing)
        
        for i in range(len(security)):
            
#             nd = non_decreasing[i]  if time != 1  else non_decreasing[i] - 1
#             ni = non_increasing[i]  if time != 1 else non_increasing[i] - 1
#             print(i,ni,nd)
            # if nd > time and ni > time:
            #     output.append(i)
            if i - time >= 0 and len(security) - 1 -i >= time and non_increasing[i]>= time and non_decreasing[i]>= time:
                output.append(i)
        
        
                
        return output
        
        