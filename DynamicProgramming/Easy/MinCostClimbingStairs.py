from typing import List


class Solution:
    def __init__(self):
        self.memo = []  # Memoization array.

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.memo = [0] * n  # Initialize memo array to size of cost array
        return min(self.rec(cost, n-1), self.rec(cost, n-2))

    def rec(self, cost, n):
        if n < 0:
            return 0  # This is the empty list, or list of one case?
        if n == 0 or n == 1:  # Base cases to handle getting to the end.
            return cost[n]
            # Since the parent call is weighing the two ops
            # then we'll be able to see which of the two were more efficient.

        # The memoization here short circuits the recursive calls, so it
        # doesn't have to brute force its way through every calculation right
        # back to the beginning of the array.
        if self.memo[n] != 0:
            return self.memo[n]

        # The next part works on filling in the memo which is just as important
        # as the recursive call itself.

        # Find the cost of the current index plus the minimum of its next
        # two options.
        self.memo[n] = cost[n] + min(self.rec(cost, n-1), self.rec(cost, n-2))

        return self.memo[n]


def main():
    solution = Solution()
    cost = [10, 15, 20]
    cost = [0, 1, 2, 2]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(solution.minCostClimbingStairs(cost))


if __name__ == '__main__':
    main()
