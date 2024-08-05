class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for l in range(len(s)):
            if l < len(s) - 1:
                leftscore = s[:l+1].count("0")
                rightscore = s[l+1:].count("1")
                result = max(result, leftscore + rightscore)
        return result