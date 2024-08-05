class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        runningsum = 0
        remainder_freq =  {0 : 1}
        count  = 0
        for num in nums:
            runningsum += num
            remainder = runningsum % k
            
            if remainder in remainder_freq:
                count += remainder_freq[remainder]
                remainder_freq[remainder] += 1
            
            else:
                remainder_freq[remainder] = 1
        return count