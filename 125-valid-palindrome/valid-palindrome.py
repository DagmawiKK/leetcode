class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = list(map(str.lower, filter(str.isalnum, s)))
        print(array)

        return "".join(array) == "".join(reversed(array))
