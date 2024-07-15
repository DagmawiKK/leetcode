class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        expensive = max(costs)
        
        count = [0] * (expensive + 1)
        
        for cost in costs:
            count[cost] += 1
        
        result = 0
        
        for i in range(1, expensive + 1):
            if count[i] > 0:
                if coins >= i * count[i]:
                    result += count[i]
                    coins -= i * count[i]
                else:
                    result += coins // i
                    coins = 0
                    break
        return result