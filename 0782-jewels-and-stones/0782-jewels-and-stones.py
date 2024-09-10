class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(list(stones))

        result = 0

        for char in jewels:
            if char in count:
                result += count[char]

        return result