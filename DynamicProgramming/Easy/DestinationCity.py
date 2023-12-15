from typing import List


# Starter code given below:
class Solution:
    def destCity(self, paths: List[List[str]], i: int) -> str:
        # Memoizations
        departures = set()
        arrivals = set()

        # Base case, if you're at the end of the list, subtract the destination
        # set from the arrivals, then return whatever is in it.
        if i > len(paths) - 1:
            city = arrivals - departures
            return city.pop()








# Testing:
def main():
    pass

if __name__ == "__main__":
    main()