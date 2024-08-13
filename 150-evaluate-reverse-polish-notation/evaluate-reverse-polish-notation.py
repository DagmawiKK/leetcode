class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"*", "/", "+", "-"}
        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                stack.append(int(eval(f"{firstNum} {i} {secondNum}")))
        return stack[0]