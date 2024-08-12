class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = len(stack)
        for i in s:
            if i == "(":
                stack.append(i)
                result = max(result, len(stack))
            if i == ")":
                stack.pop()
        return result
            
            
