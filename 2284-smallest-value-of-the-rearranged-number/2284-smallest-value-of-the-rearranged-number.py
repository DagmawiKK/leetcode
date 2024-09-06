class Solution:
    def smallestNumber(self, num: int) -> int:
        negative  = False
        if num < 0:
            negative = True
            num *= -1
        num = sorted(list(str(num)), key = lambda x : int(x))

        if negative:
            num = reversed(num)
            return -1 * int("".join(num))
        i = 0
        while i < len(num):
            if num[i] != "0":
                break
            i += 1
        result = num[i:]


        result.insert(1, "0"*i )

        return int("".join(result))
