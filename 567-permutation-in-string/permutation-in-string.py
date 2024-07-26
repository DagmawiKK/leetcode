class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        a = sorted(s1)
        for i in range(len(s2)):
            b = sorted(s2[i:i+len(s1)])
            
            if a == b:
                return True
        return False
        