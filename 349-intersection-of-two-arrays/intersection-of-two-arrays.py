class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        result = set()
        for i in nums2:
            if i not in result and i in set(nums1):
                result.add(i)
        return list(result)