class StockSpanner:
    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        span = 1
        while len(self.monotonic_stack) > 0 and self.monotonic_stack[-1][0] <= price:
            span += self.monotonic_stack.pop()[1]
        self.monotonic_stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()

# inputs = [[100], [80], [60], [70], [60], [75], [85]]
inputs = [[31],[41],[48],[59],[79]]
for i in inputs:
    print(obj.next(i[0]))