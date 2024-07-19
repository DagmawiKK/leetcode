class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sNUM = sorted(nums)
        result = []

        for i in nums:
            result.append(sNUM.index(i))
        return result