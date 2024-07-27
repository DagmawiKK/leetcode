class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        zero = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            result = max(result, right - left)
        return result