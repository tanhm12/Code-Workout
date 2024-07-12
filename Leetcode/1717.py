class Solution:

    def count(self, s: str, first: str, second: str, point: int) -> (int, str):
        if len(s) == 0:
            return 0, ""
        stack = []
        res = 0
        for c in s:
            if len(stack) > 0 and c == second and stack[-1] == first:
                res += point
                stack.pop()
            else:
                stack.append(c)
        return res, "".join(stack)


    def maximumGain(self, s: str, x: int, y: int) -> int:
        s1, s2 = "ab", "ba"
        values = {s1: x, s2: y}
        if x < y:
            s1, s2 = s2, s1
            values = {s1: y, s2: x}

        res, s = self.count(s, s1[0], s1[1], values[s1])  # remove all highest pair if possible
        return res + self.count(s, s2[0], s2[1], values[s2])[0]  # repeat with the other


if __name__ == "__main__":
    s = "cdbcbbaaabab" * int(1e4)
    x = 4
    y = 5
    print(Solution().maximumGain(s, x, y))