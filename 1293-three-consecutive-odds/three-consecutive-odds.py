class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if (len(arr) < 3):
            return False
        for i in range(0, len(arr)):
            if(arr[i] % 2 != 0):
                if((len(arr) -1 - i) >= 2):
                    if(arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0):
                        return True
                else:
                    return False
        return False