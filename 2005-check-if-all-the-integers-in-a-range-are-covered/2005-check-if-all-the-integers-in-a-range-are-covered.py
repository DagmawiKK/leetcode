class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        can = [0] * 52
        length = 0
        for s, e in ranges:
            can[s] += 1
            can[e + 1] -= 1
        
        list_m = list(accumulate(can))

        for num in range(left, right+1):
            if list_m[num] >= 1:
                length += 1 

        return length == (right - left +1)
