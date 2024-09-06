class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        bob = 0
        me = len(piles) - 2
        
        result = 0
        while bob < me:
            result += piles[me]
            me -= 2
            bob += 1

        return result