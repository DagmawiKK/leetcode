from more_itertools import sort_together
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = sort_together([indices, list(s)])
        return ''.join(result[1])
