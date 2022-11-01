class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        sortedlogs = []
        nums = []
        
        for i,log in enumerate(logs):
            lst = log.split(' ')
            if not lst[1].isnumeric():
                string = " ".join(lst[1:])
                sortedlogs.append((string,lst[0],i))
            else:
                nums.append(log)
                
        sortedlogs.sort()
        
        finallist = []
        
        for log,identifier,i in sortedlogs:
            finallist.append(logs[i])
        
        finallist.extend(nums)
        
        return finallist
                
            