class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time.sort()
        freq = defaultdict(int)
        multiples = [60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960]
        total = 0
        
        for i in range(len(time)):
            # print(freq)
            x = bisect.bisect_left(multiples,time[i])
            for j in range(x,len(multiples)):
                need = multiples[j] - time[i]
                # print(time[i],need)
                total += freq[need]
            freq[time[i]] += 1
            
        return total
                
        