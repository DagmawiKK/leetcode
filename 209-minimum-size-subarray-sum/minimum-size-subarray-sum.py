class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = 10**9
        total = 0 
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                total -= nums[left]
                result = min(result, right - left+1)
                left += 1
                
        if result == 10**9:
            return 0

        return result