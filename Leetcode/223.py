class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s1 = abs((ax1 - ax2) * (ay1 - ay2))
        s2 = abs((bx1 - bx2) * (by1 - by2))
        if max(ax1, ax2) <= min(bx1, bx2) or max(bx1, bx2) <= min(ax1, ax2) or max(ay1, ay2) <= min(by1, by2) or max(by1, by2) <= min(ay1, ay2):
            s3 = 0
        else:
            s3 = min(abs(ax1-bx2), abs(ax2-bx1), abs(ax1 - ax2), abs(bx1 - bx2)) *\
                min(abs(ay2 - by1), abs(ay1 - by2), abs(ay1 - ay2), abs(by1 - by2))
        return s1 + s2 - s3

