class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums) -1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i += 1
            i += 1

        left=0
        right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
            else:
                right += 1
        
        return nums