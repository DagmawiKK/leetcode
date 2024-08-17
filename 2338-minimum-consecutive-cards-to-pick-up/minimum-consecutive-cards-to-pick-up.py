class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        seen = set()

        result = float("inf")
        contains_duplicate = False

        for right in range(len(cards)):
            while cards[right] in seen:
                contains_duplicate = True
                seen.remove(cards[left])
                left += 1

            seen.add(cards[right])
            if contains_duplicate:
                result = min(result, right - left+2)
        
        if not contains_duplicate:
            return -1
        return result

        