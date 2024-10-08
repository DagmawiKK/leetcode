class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        left = 0
        Tcount = Fcount = result = 0

        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                Tcount += 1
            else:
                Fcount += 1
            
            while min(Tcount, Fcount) > k:
                if answerKey[left] == "T":
                    Tcount -= 1
                else:
                    Fcount -= 1
                left += 1
            result = max(result, right - left + 1)

        return result