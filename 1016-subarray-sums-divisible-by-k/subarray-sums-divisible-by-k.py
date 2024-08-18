class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_frequency = [0] * k
        remainder_frequency[0] = 1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            count += remainder_frequency[remainder]
            remainder_frequency[remainder] += 1
        return count