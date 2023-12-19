class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        fib_num = self.fib(n-1) + self.fib(n-2)
        return fib_num

def main():
    solution = Solution()
    for num in range(20):
        print(solution.fib(num))

if __name__ == '__main__':
    main()