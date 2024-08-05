class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum= 0

        r = len(nums) - 1

        total = sum(nums)

        for l in range(len(nums)):
            if leftsum != total - leftsum - nums[l]:
                leftsum += nums[l]
            else:
                return l
        return -1
                