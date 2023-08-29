class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pen = customers.count("N")
        pos = n
        cur_pen = pen
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                cur_pen += 1
            else:
                cur_pen -= 1
            cur_pen = max(0, cur_pen)
            if cur_pen <= pen:
                pen = cur_pen
                pos = i
        return pos

customers = "YYNY"
customers = "YYYYYY"
customers = "NNNN"

print(Solution().bestClosingTime(customers))
