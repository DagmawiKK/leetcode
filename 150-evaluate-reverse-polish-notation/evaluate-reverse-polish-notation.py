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
                match i:
                    case "*":
                        stack.append(firstNum * secondNum)
                        continue
                    case "+":
                        stack.append(firstNum + secondNum)
                        continue
                    case "-":
                        stack.append(firstNum - secondNum)
                        continue
                    case "/":

                        stack.append(int(firstNum / secondNum))
                        continue
        return stack[0]