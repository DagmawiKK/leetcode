class Solution:
    def validPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        i = 0
        def is_palindrome_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j + 1))
        while i < j:
            if s[i] != s[j]:
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)
            i +=1
            j -=1
        return True