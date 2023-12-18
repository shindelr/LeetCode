from typing import List


# Starter code given below:
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        total_cities = set()
        departures = set()

        # Add all cities to the total set and all departure cities to theirs.
        for item in paths:
            total_cities.add(item[0])
            total_cities.add(item[1])
            departures.add(item[0])

        # Subtract the departures from the total number of cities and return
        # the one that remains.
        final_set = set(total_cities - departures)
        return final_set.pop()

# Testing:
def main():
    solution = Solution()

    paths = [["B", "C"], ["D", "B"], ["C", "A"]]
    print(solution.destCity(paths))

    paths = [["A", "Z"]]
    print(solution.destCity(paths))


    paths = [["London", "New York"], ["New York", "Lima"],
             ["Lima", "Sao Paulo"]]
    print(solution.destCity(paths))


if __name__ == "__main__":
    main()