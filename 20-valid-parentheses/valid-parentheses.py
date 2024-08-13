class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        stack_close = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                stack_close.append(i)
            if stack and ((i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (i == "]" and stack[-1] == "[")):
                stack.pop()
                stack_close.pop()
        if stack or stack_close:
            return False
        return True

