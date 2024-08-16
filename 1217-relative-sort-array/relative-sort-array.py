class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count = Counter(arr1)

        result = []

        for i in arr2:
            result.extend([i] * count[i])
            del count[i]
        
        for i in sorted(count.keys()):
            result.extend([i]* count[i])

        return result
