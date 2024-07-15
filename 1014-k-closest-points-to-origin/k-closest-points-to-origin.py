class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(pts):
            return (pts[0] ** 2) + (pts[1] ** 2)
        points.sort(key=distance)
        return points[:k]