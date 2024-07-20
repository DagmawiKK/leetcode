class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area_max = 0
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            area_max = max(area_max, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area_max
