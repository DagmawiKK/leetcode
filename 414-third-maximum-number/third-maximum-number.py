class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        top3 = set()
        
        for num in nums:
            top3.add(num)
            
            if len(top3) > 3:
                top3.remove(min(top3))
        
        if len(top3) < 3:
            return max(top3)
        
        return min(top3)
