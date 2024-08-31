class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        countZero = 0
        prod = 1

        for num in nums:
            if num == 0:
                countZero += 1
            else:
                prod *= num
        
        answer = [0] * len(nums)

        if countZero > 1:
            return answer
        
        if countZero == 1:
            answer[nums.index(0)] = prod
            return answer

        for i in range(len(nums)):
            answer[i] = prod // nums[i]

        return answer
