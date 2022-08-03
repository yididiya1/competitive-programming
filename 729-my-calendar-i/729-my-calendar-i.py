class MyCalendar:

    def __init__(self):
        self.events = []
    
    
    def book(self, start: int, end: int) -> bool:
        def check_double(s1,e1,s2,e2):
            if s2 >= e1 and e2 >= e1:
                return True
            elif s2 <= s1 and e2 <= s1:
                return True
            return False
        
        if not self.events:
            self.events.append((start,end))
            return True
        else:
            for s,e in self.events:
                if not check_double(s,e,start,end):
                    return False
            
            self.events.append((start,end))
            return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)