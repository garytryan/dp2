# The top down dynamic programming approach uses the recursive algorithm, and saves the result of each recursion to a cache.
# The recursive function then checks the cache to see if the sub problem have already been computed.

def solution(profit: [int], weight: [int], capacity: int) -> int:
    def combinations(profit: [int], weight: [int], capacity: int, currentItemIndex: int, cache: {int: int}) -> [int]:
        numberOfItems = len(profit)

        if currentItemIndex == numberOfItems or capacity == 0:
            return 0

        for i in range(currentItemIndex, numberOfItems):
            # Check the cache, return the result if one exists
            if cache[i][capacity]:
                return cache[i][capacity]

            itemWeight = weight[i]

            profitWithItem = 0
            if itemWeight <= capacity:
                profitWithItem = profit[currentItemIndex] + combinations(profit, weight, capacity - itemWeight, currentItemIndex + 1, cache)

            profitWithoutItem = combinations(profit, weight, capacity, currentItemIndex + 1, cache)

            # Add the result to the cache
            cache[i][capacity] = max(profitWithItem, profitWithoutItem)

            return cache[i][capacity]

    # Create the cache
    cache = [[None]*(capacity+1) for _ in range(len(profit))]
    return combinations(profit, weight, capacity, 0, cache)
