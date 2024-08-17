class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = 10**9
        total = 0 
        for right in range(len(nums)):
            total += nums[right]
            if total >= target:
                result = min(result, right - left+1)
            while total >= target:
                total -= nums[left]
                left += 1
                result = min(result, right - left+2)
                
        if result == 10**9:
            return 0

        return result