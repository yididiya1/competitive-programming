class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        
        def adder(sticker,w): 
            for c in sticker: 
                w = w.replace(c,'',sticker[c])
            return w
        
        @lru_cache(None)
        def dfs(s): 
            if not s: 
                return 0
            res = float('inf')
            for sticker in stickers: 
                if s[0] not in sticker: 
                    continue 
                w = adder(sticker,s) 
                res = min(res,1 + dfs(w)) 
            return res
        
        stickers = [Counter(s) for s in stickers]
        res = dfs(target) 
        return res if res!=float('inf') else -1
