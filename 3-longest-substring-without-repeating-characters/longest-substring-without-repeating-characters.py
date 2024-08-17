class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        seen = deque()
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.popleft()
                left+=1
            seen.append(s[right])
            result = max(result, right - left + 1)
        return result