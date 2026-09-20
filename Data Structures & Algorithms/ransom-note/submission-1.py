class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        countR = Counter(ransomNote)
        countM = Counter(magazine)

        if len(countM) < len(countR):
            return False

        for char in countR:
            if countR[char] > countM[char]:
                return False
        
        return True
        
