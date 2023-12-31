from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        num_units = 0
        boxTypes.sort(key=lambda x: -x[1])  # Sorts the list into descending order by number of units per box

        for obj in boxTypes:
            if obj[0] < truckSize:
                num_units += obj[1] * obj[0]
                truckSize -= obj[0]
            else:
                num_units += truckSize * obj[1]
                return num_units


if __name__ == '__main__':
    soln = Solution()
    print(soln.maximumUnits([[5,10],[2,5],[4,7],[3,9]], truckSize = 10))