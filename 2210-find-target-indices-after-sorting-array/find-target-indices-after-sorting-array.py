class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        try:
            result.append(nums.index(target))
        except ValueError:
            return []
        val = nums.index(target) + 1

        while val < len(nums)and nums[val] == target :
            result.append(result[-1] + 1)
            val += 1
        return result
