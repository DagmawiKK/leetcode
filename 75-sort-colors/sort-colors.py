class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 1, 2]
        left = 0

        for i in range(len(colors)):
            right = 0
            while right < len(nums):
                if nums[right] == colors[i]:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                    left += 1
                right += 1