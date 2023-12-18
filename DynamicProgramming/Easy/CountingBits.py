from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        memo = ans

        for i in range(0, n+1):
            ans[i] = self.count_bits_rec(i, memo)

        return ans


    def count_bits_rec(self, n, memo):
        # Two base cases:
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Deal with memo
        if memo[n] != 0:
            return memo[n]  # We've already calculated it
        if n % 2 == 0:  # If even,
            memo[n] = self.count_bits_rec(n//2, memo)
            return self.count_bits_rec(n//2, memo)

        else:  # If odd, add one to the calculation to set the rightmost bit?
            memo[n] = 1 + self.count_bits_rec(n//2, memo)
            return 1 + self.count_bits_rec(n//2, memo)


def main():
    solution = Solution()

    print(solution.countBits(5))

if __name__ == '__main__':
    main()
