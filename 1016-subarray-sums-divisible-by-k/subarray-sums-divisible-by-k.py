class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        remainder_f = {0:1}
        total = 0
        for index in range(len(nums)):
            total += nums[index]
            remainder = total % k
            if remainder in remainder_f:
                count += remainder_f[remainder]
                remainder_f[remainder] += 1
            else:
                remainder_f[remainder] = 1
        return count