class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = 101
        current = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                current += 1
        
        minimum = min(minimum, current)
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current -= 1
            if blocks[i] == 'W':
                current += 1
            minimum = min(minimum, current)
        
        return minimum

