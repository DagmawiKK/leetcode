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
                if i == "*":
                    stack.append(firstNum * secondNum)
                elif i == "+":
                    stack.append(firstNum + secondNum)
                elif i == "-":
                    stack.append(firstNum - secondNum)
                else:
                    stack.append(int(firstNum / secondNum))
        return stack[0]