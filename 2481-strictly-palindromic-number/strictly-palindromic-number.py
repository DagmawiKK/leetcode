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
            if len(string_rep) % 2 != 0: return False
            left = 0
            right = len(string_rep) - 1
            
            while left < right:
                if string_rep[left] != string_rep[right]:
                    return False
                left += 1
                right -=1
        return True