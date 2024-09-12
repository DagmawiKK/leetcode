class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        nott = False
        for word in words:
            for char in set(word):
                if char not in allowed:
                    nott = True
                    break
            if not nott:
                count += 1
            nott =False
        return count
