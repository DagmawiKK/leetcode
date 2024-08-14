class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum = 0
        total = sum(nums)
        for left in range(len(nums)):
            if leftsum == total - leftsum - nums[left]:
                return left
            leftsum += nums[left]
        return -1 
        