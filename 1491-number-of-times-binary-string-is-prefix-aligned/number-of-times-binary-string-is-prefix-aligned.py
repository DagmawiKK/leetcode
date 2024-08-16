class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        array = [0]*len(flips)
        count = 0
        for i in range(len(array)):
            array[flips[i]-1] = 1
            try:
                if array.index(0) > i:
                    count += 1
            except:
                count += 1
        return count