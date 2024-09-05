class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        right_most_on = 0
        for i in range(len(flips)):
            right_most_on = max(right_most_on, flips[i])
            if right_most_on == i+1:
                count += 1
        return count