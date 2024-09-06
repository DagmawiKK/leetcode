class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for coin in costs:
            if coins >= 0:
                coins -= coin
                count += 1
        return count if coins >= 0   else count-1
