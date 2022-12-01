import bisect
class Solution:
    _primes = [2]
    _max = int(5e6)+1
    _cands = [True] * _max
    _cands[0] = _cands[1] = False
    for i in range(2, int(_max**0.5)+1):
        if _cands[i]:
            # _primes.append(i)
            _cands[i * i:_max:i] = [False] * len(_cands[i * i:_max:i])
    def countPrimes(self, n: int) -> int:
        primes = self._primes
        if n <= primes[-1]:
            return bisect.bisect_left(primes, n)
        else:
            for i in range(primes[-1] + 1, n):
                if self._cands[i]:
                    primes.append(i)
            return len(primes)

        # return sum(self._cands[:n])
        

sol = Solution()

while True:
    print(sol.countPrimes(int(input())))
