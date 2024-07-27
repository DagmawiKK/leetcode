class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return 0
            else:
                return len(nums)-1
        if nums.count(0) == 1:
            return len(nums) - 1
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