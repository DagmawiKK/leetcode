class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        try:
            result.append(nums.index(target))
        except ValueError:
            return []
        for i in range(nums.index(target) + 1, len(nums)):
            if nums[i] == target:
                result.append(i)
            else:
                break
        return result