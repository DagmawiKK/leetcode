class Solution:
    def __init__(self):
        self.seen = {}
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 3:
            return False
        elif n in self.seen:
            return seen[n]
        
        self.seen[n] = self.isPowerOfThree(n / 3)
        return self.seen[n]