class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = float('inf')
        total = 0 
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                total -= nums[left]
                result = min(result, right - left+1)
                left += 1
                
        if result == float('inf'):
            return 0

        return result