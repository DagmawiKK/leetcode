class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            middle = low + ((high - low) // 2)
            if target < nums[middle]:
                high = middle
            elif target > nums[middle]:
                low = middle + 1
            elif target == nums[middle]:
                return middle
        return -1