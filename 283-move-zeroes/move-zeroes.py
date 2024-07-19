class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 2, 0, 3, 4, 0, 5]
        # j = 0
        # i = 0

        j = 0
        k = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
