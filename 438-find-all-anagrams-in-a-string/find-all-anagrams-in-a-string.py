class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return ""
        result = []
        a = sorted(p)
        for i in range(len(s) - len(p)+1):
            b = sorted(s[i:i+len(p)])
            if a == b:
                result.append(i)
        return result