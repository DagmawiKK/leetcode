class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        mark_pt = sum(arr) / 3
        count = running_sum = 0

        for i in range(len(arr)):
            running_sum += arr[i]

            if running_sum == mark_pt:
                count += 1
                running_sum = 0

        return True if count >= 3 else False
