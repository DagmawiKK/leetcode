class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        try:
            result.append(nums.index(target))
        except ValueError:
            return []
        
        count = nums.count(target)

        for i in range(count - 1):
            result.append(result[-1] + 1)
        return result
