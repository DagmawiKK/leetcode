class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        stack = []

        result = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:

                height = heights[stack.pop()]
                if stack:
                    result = max(result, height * (i - stack[-1] -1) )
                else:
                    result = max(result, height * (i))
                
            stack.append(i)

        while stack:

            height = heights[stack.pop()]
            if stack:
                result = max(result, height * (len(heights) - stack[-1] -1) )
            else:
                result = max(result, height * len(heights) )

        return result
