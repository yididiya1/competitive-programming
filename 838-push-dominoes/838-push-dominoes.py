class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dominoes= list(dominoes)
        
        queue = deque([])
        
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                queue.append((dominoes[i],i))
        level = set()
        while queue:
            n = len(queue)            
            for i in range(n):
                dxn,idx = queue.popleft()
                level.add(idx)
                if dxn == 'L':
                    if idx - 1 >= 0  and dominoes[idx - 1] == '.':
                        if idx - 2 < 0:
                            dominoes[idx-1] = 'L'
                            queue.append(('L',idx-1))
                        elif idx - 2 >= 0 and ( dominoes[idx - 2] != 'R' or (dominoes[idx - 2] == 'R' and idx-2 not in level)) :
                            dominoes[idx-1] = 'L'
                            queue.append(('L',idx-1))
                else:
                    if idx + 1 < len(dominoes)  and dominoes[idx + 1] == '.':
                        if idx + 2 >= len(dominoes):
                            dominoes[idx+1] = 'R'
                            queue.append(('R',idx+1))
                        elif idx + 2 < len(dominoes) and ( dominoes[idx + 2] != 'L' or ( dominoes[idx+2] == 'R' and idx+2 not in level)):
                            dominoes[idx+1] = 'R'
                            queue.append(('R',idx+1))

                  
        return "".join(dominoes)