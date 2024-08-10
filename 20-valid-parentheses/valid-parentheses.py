class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack2 =[]
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                try:
                    if s[i] == ")" and stack[-1] == "(":
                        stack.pop()
                    elif s[i] == "}" and stack[-1] == "{":
                        stack.pop()

                    elif s[i] == "]" and stack[-1] == "[":
                        stack.pop()

                    else:
                        return False
                except:
                    return False
        if len(stack) == 0:
            return True 
        return False