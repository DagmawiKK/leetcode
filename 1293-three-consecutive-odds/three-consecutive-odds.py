class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        for i in arr:
            if(i % 2 != 0):
                if((len(arr)-1 - arr.index(i)) >= 2):
                     if arr[arr.index(i)+1] %2 !=0 and arr[arr.index(i)+2] %2 !=0:
                        return True
                else:
                    return False
        return False