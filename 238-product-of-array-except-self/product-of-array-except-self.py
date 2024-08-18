class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = 1
        answer = [1] * n

        for i in range(n):
            answer[i] = temp
            temp *= nums[i]

        temp = 1

        for j in range(n-1, -1, -1):
            answer[j] *= temp
            temp *= nums[j]

        return answer
        
