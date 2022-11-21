from heapq import heappush, heappop, heappushpop

class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.right_heap) == 0:
            heappush(self.right_heap, num)
            return
        right = self.right_heap[0]
        if num <= right:
            if len(self.left_heap) > len(self.right_heap):
                val = -heappushpop(self.left_heap, -num)
                heappush(self.right_heap, val)
            else:
                heappush(self.left_heap, -num)
        else:
            if len(self.right_heap) > len(self.left_heap):
                val = heappushpop(self.right_heap, num)
                heappush(self.left_heap, -val)
            else:
                heappush(self.right_heap, num)


    def findMedian(self) -> float:
        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        elif len(self.right_heap) < len(self.left_heap):
            return -self.left_heap[0]
        else:
            return (self.right_heap[0] - self.left_heap[0]) / 2