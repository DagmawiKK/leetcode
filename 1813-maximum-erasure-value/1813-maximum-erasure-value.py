class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        total = left = 0
        seen = set()
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1
            total += nums[right]
            seen.add(nums[right])
            res = max(res, total)
        return res