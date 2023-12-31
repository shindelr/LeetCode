class Solution:
    def maximum69Number(self, num: int) -> int:
        string_num = list(str(num))
        for i in range(len(string_num)):
            if string_num[i] == '6':
                string_num[i] = '9'
                output = ''.join(string_num)
                return int(output)
        return num



if __name__ == '__main__':
    soln = Solution()
    print(soln.maximum69Number(99))