class Solution:
    def reverseParentheses(self, s: str) -> str:
        def helper(index):
            result = []
            while index < len(s):
                if s[index] == '(':
                    substring, index = helper(index + 1)
                    result.extend(substring[::-1])
                elif s[index] == ')':
                    return result, index
                else:
                    result.append(s[index])
                index += 1
            return result, index

        final_result, _ = helper(0)
        return ''.join(final_result)