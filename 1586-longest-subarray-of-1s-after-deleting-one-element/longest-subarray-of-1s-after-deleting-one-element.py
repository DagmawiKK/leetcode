class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        count = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            
            result = max(result, right - left)

        return result
