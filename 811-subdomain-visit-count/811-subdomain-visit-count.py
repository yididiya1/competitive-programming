class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = defaultdict(int)
        
        
        for cpdomain in cpdomains:
            count,domain = cpdomain.split(" ")        
            l = 0 
            r = len(domain)
            
            freq[domain] += int(count)
            
            while l < r:
                if domain[l] != '.':
                    l += 1
                else:
                    freq[domain[l+1:]] += int(count)
                    l += 1
        
        # print(freq)
        answer = []
        for domain,count in freq.items():
            y = [str(count),domain]
            x = " ".join(y)
            answer.append(x)
            
        return answer
        