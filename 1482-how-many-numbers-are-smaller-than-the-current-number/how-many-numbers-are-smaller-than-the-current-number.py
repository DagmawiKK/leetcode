class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        
        smaller_count = {}
        
        for i, num in enumerate(arr):
            if num not in smaller_count:
                smaller_count[num] = i
        
        result = [smaller_count[num] for num in nums]
        return result

