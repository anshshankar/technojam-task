class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        size=len(points)
        total=0
        for i in range(size-1):
            x=abs(points[i][0]-points[i+1][0])
            y=abs(points[i][1]-points[i+1][1])
            total+=max(x,y)
        return total
