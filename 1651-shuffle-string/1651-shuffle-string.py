class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        for i, index in enumerate(indices):
            res[index] = s[i] 
        return "".join(res) 