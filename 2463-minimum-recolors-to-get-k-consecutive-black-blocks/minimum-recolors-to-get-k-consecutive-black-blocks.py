class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        operation = blocks[:k].count("W")
        result = operation
        left = 0
        for right in range(k, len(blocks)):
            if blocks[left] == "W":
                operation -= 1
            if blocks[right] == "W":
                operation += 1
            left += 1
            result = min(result, operation)
        return result
