class Solution:
    def __init__(self):
        # Initialize a memoization map to significantly reduce recursive calls.
        self.memo = {}

    def fib(self, n: int) -> int:
        # Base cases for when you need to calculate a number not in the map.
        if n == 0:
            return 0
        if n == 1:
            return 1

        # If able to access both n-1 & n-2, no need to make a recursive call.
        # Simply access the values stored in the memo and compute the new fib
        # number. Don't forget to add the new number and its corresponding
        # place to the memo map in either case.
        if n-1 in self.memo and n-2 in self.memo:
            fib_num = self.memo[n-1] + self.memo[n-2]
            self.memo[n] = fib_num
        else:
            fib_num = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = fib_num
        return fib_num


def main():
    solution = Solution()
    for num in range(20):
        print(solution.fib(num))


if __name__ == '__main__':
    main()