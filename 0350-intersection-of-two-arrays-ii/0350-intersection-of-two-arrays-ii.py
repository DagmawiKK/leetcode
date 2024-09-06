class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        for num in nums1:
            if num not in result:
                result.extend([num] * min(count1[num], count2[num]))
        
        return result


