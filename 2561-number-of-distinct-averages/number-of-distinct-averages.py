class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        avg = set()

        while len(nums) > 1:
            avg.add((nums[-1] + nums[0])/2)
            nums.pop()
            nums.pop(0)
        return len(avg)