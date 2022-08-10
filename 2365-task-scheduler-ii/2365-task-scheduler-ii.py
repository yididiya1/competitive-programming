class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        
        time = 0
        startTime  = {}
        
        for i in range(len(tasks)):
            # print(time,tasks[i],startTime)
            if tasks[i] not in startTime:
                time += 1
                startTime[tasks[i]] = time+space+1
            else:
                needed = startTime[tasks[i]]
                if needed <= time:
                    time += 1   
                else:
                    time += needed - time
                startTime[tasks[i]] = time + space  +1 
                
        return time
            
        