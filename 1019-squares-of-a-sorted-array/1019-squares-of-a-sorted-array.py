class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        right = len(nums) - 1
        left = 0
        while left <= right:
            if -1 * nums[left] > nums[right]:
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        return reversed(result)