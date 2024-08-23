class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        result = [-1]*n

        for i in range(n*2):
            num = nums[i%n]

            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            
            if i < n:
                stack.append(i)

        return result
