class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        
        for index, num in enumerate(nums):
            if num in index_map:
                if abs(index_map[num] - index) <= k:
                    return True
            index_map[num] = index
        return False
            
