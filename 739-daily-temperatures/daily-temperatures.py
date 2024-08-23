class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i, temp in enumerate(reversed(temperatures)):
            while stack and stack[-1][1] <= temp:
                print(stack[-1])
                stack.pop()
            if stack:
               
                result.append(i - stack[-1][0])
            else:
                result.append(0)

            stack.append((i, temp))
        return reversed(result)


        # 1 100
        # 2 76
        # 
        # 5 47


        # 0 0 1 1 2





            