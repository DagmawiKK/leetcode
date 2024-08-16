class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = list(map(str.lower, filter(lambda x: x.isalpha() or x.isnumeric(), s)))
        print(array)

        return "".join(array) == "".join(reversed(array))
