class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1 = defaultdict(int)
        set2 = set(arr2)
        end = []

        res = []

        for num in arr1:
            if num not in set2:
                end.append(num)
            else:
                count1[num] += 1
        end.sort()
        for num in arr2:
            while count1[num] > 0:
                res.append(num)
                count1[num] -= 1

        res.extend(end)
        
        return res
