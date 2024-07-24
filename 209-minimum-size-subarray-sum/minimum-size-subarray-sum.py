class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = 10**5 + 1
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_length == 10**5 + 1 else min_length