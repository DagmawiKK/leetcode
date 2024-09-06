class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = 0
        points = sorted(points, key = lambda x : x[0])
        
        for i in range(1, len(points)):
            start_f, end_f = points[i-1]
            start, end = points[i] 
            res = max(res, start - start_f)

        return res
