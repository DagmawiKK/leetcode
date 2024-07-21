class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 in set(arr):
            i = 0
            while i < len(arr):
                if arr[i] == 0 and i < len(arr)-1:
                    arr.insert(i + 1, 0)
                    arr.pop()
                    i += 2
                else:
                    i += 1


