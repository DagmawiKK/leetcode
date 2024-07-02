class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        result = []
        i = 0
        if(len(nums1) <= len(nums2)):
            for item in nums1:
                if item in nums2:
                    result.append(item)
                    nums2[nums2.index(item)] = '-'
        else:
            for item in nums2:
                if item in nums1:
                    result.append(item)
                    nums1[nums1.index(item)] = '-'
        return result