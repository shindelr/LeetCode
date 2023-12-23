class Solution:
    def __init__(self):
        self._memo = {0:0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        if n-1 in self._memo and n-2 in self._memo and n-3 in self._memo:
            trib = self._memo[n-1] + self._memo[n-2] + self._memo[n-3]
            self._memo[n] = trib
        else:
            trib = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self._memo[n] = trib

        return trib

if __name__ == '__main__':
    sol = Solution()

    n = 25
    print(sol.tribonacci(n))
