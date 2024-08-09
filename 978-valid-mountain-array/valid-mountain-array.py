class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        mymax = max(arr)
        if arr.count(mymax) != 1:
            return False

        left = 1
        right = len(arr) - 2

        while left < right:
            if arr[left] != mymax:
                if arr[left] > arr[left - 1]:
                    left += 1
                else:
                    return False
            if arr[right] != mymax: 
                if arr[right] > arr[right + 1]:
                    right -= 1
                else:
                    return False
        return True
