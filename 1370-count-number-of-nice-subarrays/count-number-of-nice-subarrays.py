class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0 
        result = 0
        subarray_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                count += 1
                subarray_count = 0
            while count >= k:
                subarray_count += 1
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1
            result += subarray_count
        return result