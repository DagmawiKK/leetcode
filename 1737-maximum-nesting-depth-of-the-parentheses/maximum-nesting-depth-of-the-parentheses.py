class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = len(stack)
        for i in s:
            if i == "(":
                stack.append(i)
            if i == ")":
                stack.pop()
            result = max(result, len(stack))
            
        return result
            
            
