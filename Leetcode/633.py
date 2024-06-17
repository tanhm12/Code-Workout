from math import sqrt, ceil

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <=2:
            return True
        upper = round(sqrt(c))
        if upper ** 2 > c:
            upper -= 1
        for i in range(upper+1):
            ip2 = i**2
            if ip2 >= c: return False
            if round(ip2 + round(sqrt(c-ip2)) ** 2) == c:
                # print(i, round(sqrt(c-ip2)))
                return True

        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(8))