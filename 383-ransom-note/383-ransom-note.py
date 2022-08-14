class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)

        for key in rCounter:
            if key not in mCounter or rCounter[key] > mCounter[key]:
                return False
        return True
            
        