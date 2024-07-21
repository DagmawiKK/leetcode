class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()

        while len(nums) > 1:
            avg.add((max(nums) + min(nums))/2)
            nums.pop(nums.index(min(nums)))
            nums.pop(nums.index(max(nums)))
        return len(avg)