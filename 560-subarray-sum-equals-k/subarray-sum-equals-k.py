class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}

        cumulative = 0

        count = 0

        for num in nums:
            cumulative += num

            if cumulative - k in freq:
                count += freq[cumulative - k]

            freq[cumulative] = freq.get(cumulative, 0) + 1

        return count