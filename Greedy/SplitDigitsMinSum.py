from typing import List


class Solution:
    def minimumSum(self, num: int) -> int:
        digits: List[str] = sorted(str(num))
        return int(digits[0] + digits[2]) + int(digits[1] + digits[3])


if __name__ == '__main__':
    soln = Solution()
    print(soln.minimumSum(2329))