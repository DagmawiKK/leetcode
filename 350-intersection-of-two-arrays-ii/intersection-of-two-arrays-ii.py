from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        result = []
        

        # the above lines are equivalent to:
        for num in nums2:
            if num in nums1:
                result.append(num)
                nums1[nums1.index(num)] = '-' # Set it to some arbrtriary value that isn't in nums2
                
        return result