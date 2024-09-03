class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            all_small = False
            all_caps = False
            for s in range(1, len(word)):
                if word[s].islower():
                    all_small = True
                else:
                    all_caps = True
                    if all_small:
                        return False
            if all_small and all_caps:
                return False
        else:
            for s in range(len(word)):
                if word[s].isupper():
                    return False
        return True
        