class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_f = {0:1}

        count = 0 

        cumulative = 0

        for num in nums:

            cumulative += num
            remainder = cumulative % k

            if remainder in remainder_f:
                count += remainder_f[remainder]

            remainder_f[remainder] = remainder_f.get(remainder, 0) + 1

        return count