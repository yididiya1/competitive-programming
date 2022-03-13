class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # banned = set()
        dire = deque()
        radiant = deque()
        
        
        
        
        for i in range(len(senate)):
            if senate[i] == 'D':
                dire.append(i)
            else:
                radiant.append(i)
                
        while dire and radiant:
            d = dire.popleft()
            r = radiant.popleft()
            
            if d < r:
                dire.append(d+len(senate))
            else:
                radiant.append(r+len(senate))
           
           
            
        
        if len(dire) > len(radiant):
            return 'Dire'
        else:
            return 'Radiant'
                
                
        