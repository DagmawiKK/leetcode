class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        def worker(larger, smaller):
            result = []
            for item in smaller:
                if item in larger:
                    result.append(item)
                    larger[larger.index(item)] = '-'
            return result
        if(len(nums1) <= len(nums2)):
            return worker(nums2, nums1)
        else:
            return worker(nums1, nums2)
        return result 