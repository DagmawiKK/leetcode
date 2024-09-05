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
            if arr[left] < arr[left + 1]:
                left += 1
            else:
                if arr[left] != maxx:
                    return False
                elif arr[right] == maxx and arr[right-1] ==  maxx:
                    return False

            if arr[right] < arr[right-1]:
                right-= 1
            else:
                if arr[right] != maxx:
                    return False
                elif arr[right] == maxx and arr[right-1] ==  maxx:
                    return False
        return True


        return True


