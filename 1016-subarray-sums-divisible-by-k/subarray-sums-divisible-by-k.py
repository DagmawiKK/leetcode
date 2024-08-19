class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_f = {0:1}

        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            if remainder in remainder_f:
                count += remainder_f[remainder]
                remainder_f[remainder] += 1
            else:
                remainder_f[remainder] = 1

        return count