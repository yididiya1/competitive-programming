class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = set()
        target = len(arr) - 1
        occurence = {}
        for i in range(len(arr)):
            if arr[i] not in occurence:
                occurence[arr[i]] = [i]
            else:
                occurence[arr[i]].append(i)
                
        queue = deque()
        queue.append((0,0))
        
        while queue:
            index,step = queue.popleft()
            # print(index,step)
            
            if index == target:
                return step
            
            
            portal = occurence[arr[index]]
            visited.add(index)
            
            for i in range(len(portal)):
                if portal[i] not in visited:
                    queue.append((portal[i],step+1))
            
            occurence[arr[index]] = []
            
            if  0 <= index + 1 < len(arr) and index+1 not in visited:
                queue.append((index+1,step+1))
            
            if 0 <= index -1 < len(arr) and index-1 not in visited:
                queue.append((index-1,step+1))
            
            
                    
        
            
                    
        