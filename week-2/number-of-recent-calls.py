class RecentCounter:

    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        counter = 0
        
        self.requests.append(t)
        sizecounter = len(self.requests) - 1
        while sizecounter >= 0:
            if t-3000 <= self.requests[sizecounter] <= t:
                counter += 1
            else :
                return counter
            
            sizecounter -= 1
        
        return counter


obj = RecentCounter()
param_1 = obj.ping(1)
print(param_1)