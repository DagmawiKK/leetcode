class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        a = 0
        while a < len(nums) - 1:
            if nums[a] == nums[a + 1]:
                nums[a] = nums[a] * 2
                nums[a + 1] = 0
            a +=1

        b = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[b], nums[i] = nums[i], nums[b]
                b += 1
        return nums