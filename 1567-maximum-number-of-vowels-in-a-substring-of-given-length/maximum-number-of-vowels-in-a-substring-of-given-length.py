class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count = 0
        vowels = {"a","e","i","o","u"}

        for i in range(k):
            if s[i] in vowels:
                count += 1
        result = count

        for right in range(k, len(s)):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            result = max(result, count)
            left += 1

        return result

