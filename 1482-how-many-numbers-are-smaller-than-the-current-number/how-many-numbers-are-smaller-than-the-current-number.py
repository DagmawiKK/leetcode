class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)
        sort_nums = sorted(nums)

        for i in range(len(nums)):
            result[i] = sort_nums.index(nums[i])
        return result

