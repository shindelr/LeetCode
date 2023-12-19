from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base, if you've hit the bottom, time to start back up.
        if numRows == 1:
            return [[1]]

        # Otherwise, begin generating rows:
        # Decrement numRows each time so that eventually we hit the base
        # and come back up the stack.
        triangle = self.generate(numRows-1)

        # Initialize rows to be used in the current call. The previous row is
        # the row directly above the row being generated. The row being
        # generated starts with a 1 and also ends with a 1, so we'll append
        # that at the end.
        prev_row = triangle[-1]
        new_row = [1]

        # Start at 1 since index 0 is always filled. Stop before the end of the
        # previous row in order to avoid indexing issues.
        for i in range(1, len(prev_row)):
            # Append the sum of the two numbers directly above the current index.
            new_row.append(prev_row[i-1] + prev_row[i])

        # Rows always end with a 1.
        new_row.append(1)
        # Update the triangle to include the newly generated row.
        triangle.append(new_row)
        # Return triangle at the end of each call coming off the stack to
        # continuously generate rows.
        return triangle


def main():
    solution = Solution()
    print(solution.generate(5))

if __name__ == '__main__':
    main()