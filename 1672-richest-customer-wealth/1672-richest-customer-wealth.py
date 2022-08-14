class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        _max = 0
        for row in accounts:
            _sum = 0
            for i in row:
                _sum += i
            _max = max(_sum,_max)
        return _max