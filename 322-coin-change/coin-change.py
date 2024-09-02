class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(remaining):

            if remaining == 0:
                return 0

            if remaining < 0:
                return float("inf")

            minn = float("inf")

            for i in range(len(coins)-1, -1, -1):
                result = helper(remaining - coins[i])
                if result != float('inf'):
                    minn = min(minn, result + 1)
            return minn

        result = helper(amount)
        return result if result != float('inf') else -1