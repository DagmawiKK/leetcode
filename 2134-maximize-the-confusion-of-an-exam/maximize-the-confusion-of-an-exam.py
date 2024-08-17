class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        Tcount = answerKey.count("T")
        Fcount = answerKey.count("F")

        def convertor(toConvert):
            left = 0
            count = 0
            result = 0

            for right in range(len(answerKey)):
                if answerKey[right] == toConvert:
                    count += 1
                    while count > k:
                        if answerKey[left] == toConvert:
                            count -= 1
                        left += 1
                result = max(result, right - left + 1)

            return result 

        return max(convertor("T"), convertor("F"))