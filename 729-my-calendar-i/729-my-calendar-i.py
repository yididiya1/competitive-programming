class MyCalendar:

    def __init__(self):
        self.events =[]
    
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
            index = bisect_right(self.events,(start,end))
            prev = self.events[index - 1] if index - 1 >= 0 else None
            curr = self.events[index] if index < len(self.events) else None
            # print(index)
            if curr == None:
                if prev[1] <= start:
                    self.events.append((start,end))
                    return True
                else:
                    return False
            elif prev == None:
                if curr[0] >= end:
                    self.events.insert(index,(start,end))
                    return True
                else:
                    return False
            else:
                if curr[0] >= end and prev[1] <= start:
                    self.events.insert(index,(start,end))
                    return True
                else:
                    return False
           
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)