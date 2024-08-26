class Solution:
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fib(n-1)+self.fib( n-2)
        return self.memo[n]
        
