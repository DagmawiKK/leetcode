class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def converter(n, i):
            if n == 0:
                return '0'
            nums = []
            while n:
                n, r = divmod(n, i)
                nums.append(str(r))
            return ''.join(reversed(nums))
        for i in range(2, n-1):
            string_rep = converter(n, i)
            if string_rep != reversed(string_rep): return False
        return True