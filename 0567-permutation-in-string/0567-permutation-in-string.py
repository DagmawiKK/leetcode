class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        pCount, sCount = Counter(s1), Counter(s2[:len(s1)])

        if pCount == sCount:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            sCount[s2[right]] +=1
            sCount[s2[left]] -= 1

            if sCount[s2[left]] == 0:
                del sCount[s2[left]]
            
            if sCount == pCount:
                return True
            
            left += 1
        
        return False