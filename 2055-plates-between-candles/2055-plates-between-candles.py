class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = [0 for i in range(len(s))]
        prefix_sum[0] = 1 if s[0] == '|' else 0
        candles = []
        
        if s[0] == '|':
            candles.append(0)
        
        for i in range(1,len(s)):
            if s[i] == '|':
                candles.append(i)
                prefix_sum[i] = prefix_sum[i-1] + 1
            else:
                prefix_sum[i] = prefix_sum[i-1]
        
        result = []
        
        for start,end in queries:
            l = bisect_left(candles,start)
            r = bisect_right(candles,end)
            if l != r:
                sum_l = prefix_sum[candles[l]] 
                sum_r = prefix_sum[candles[r-1]]
                total = sum_r - sum_l - 1
                answer = candles[r-1] - candles[l]  - total - 1
                result.append(answer)
            else:
                result.append(0)
                
        return result
                
                                
            