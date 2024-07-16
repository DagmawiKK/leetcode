class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(0, len(nums), 2):
            if i != len(nums) -1:
                arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr
            