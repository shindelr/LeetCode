from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.rec(cost, n-1), self.rec(cost, n-2))

    def rec(self, cost, n):
        if n < 0:
            return 0  # This is the empty list, or list of one case?
        if n == 1 or n == 2:  # Base cases to handle getting to the end.
            return cost[n]
            # Since the parent call is weighing the two ops
            # then we'll be able to see which of the two were more efficient.

        # Find the cost of the current index plus the minimum of its next
        # two options.
        return cost[n] + min(self.rec(cost, n-1), self.rec(cost, n-2))


def main():
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    #cost = [10, 15, 20]
    #cost = [0, 1, 2, 2]

    print(solution.minCostClimbingStairs(cost))


if __name__ == '__main__':
    main()
