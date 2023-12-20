class Solution:
    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        return False


def main():
    solution = Solution()
    n = 3
    n = 2

    print(solution.divisorGame(n))

if __name__ == '__main__':
    main()
