class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        avg = sum(nums[:k])
        maxavg = avg
        for i in range(k, len(nums)):
            avg += -nums[i-k] + nums[i]
            if maxavg < avg:
                maxavg = avg
        return maxavg / k
