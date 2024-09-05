class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr) - 1
        maxx = max(arr)

        if arr[0] == maxx or arr[right] == maxx:
            return False
        while left < right:
            if arr[left] != maxx:
                if arr[left] < arr[left+1]:
                    left += 1
                else:
                    return False
            if arr[right] != maxx:
                if arr[right] < arr[right - 1]:
                    right -= 1
                else:
                    return False


        return True


