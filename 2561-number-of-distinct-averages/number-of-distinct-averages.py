class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        nums.sort()
        j = len(nums) - 1
        i = 0
        while i < j:
            avg.add((nums[i] + nums[j])/2)
            i += 1
            j -= 1
        return len(avg)