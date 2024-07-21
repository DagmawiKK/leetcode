class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        count = Counter(nums1)
        result = set()
        for i in nums2:
            if count[i] != 0:
                result.add(i)
                count[i] -= 1
        return list(result)