class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i += 2
                continue
            i += 1

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                if right > left:

                    nums[right] = 0
                left += 1
        return nums
        

            
