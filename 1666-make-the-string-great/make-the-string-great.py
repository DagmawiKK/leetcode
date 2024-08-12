class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):

                if stack and (s[i] == (stack[-1]).upper() or s[i] == stack[-1].lower()) and s[i] != stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])

        return ''.join(stack)
            