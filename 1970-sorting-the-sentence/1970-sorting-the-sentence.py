class Solution:
    def sortSentence(self, s: str) -> str:

        words = s.split(" ")
        words = sorted(words, key = lambda x : int(x[-1]))

        words = [word[:-1] for word in words]

        return " ".join(words)