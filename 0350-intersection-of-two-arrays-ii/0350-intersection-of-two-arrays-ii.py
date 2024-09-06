class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        checked = set()
        result = []
        for num in nums1:
            if num not in checked:
                result.extend([num] * min(count1[num], count2[num]))
            checked.add(num)
        return result


