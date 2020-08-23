def solution(profit: [int], weight: [int], capacity: int) -> int:
    # Generate all combinations of items that can fit in the knapsack
    def combinations(profit: [int], weight: [int], capacity: int, currentItemIndex: int) -> [int]:
        numberOfItems = len(profit)

        if currentItemIndex == numberOfItems or capacity == 0:
            return 0

        for i in range(currentItemIndex, numberOfItems):
            itemWeight = weight[i]

            # Add the item to the knapsack
            # If the item fits
            # Recursively call combinations
            #   with the item weight subtracted from the capacity
            #   add the profit of the item to the result of the recursive call
            #   increment the currentItemIndex
            profitWithItem = 0
            if itemWeight <= capacity:
                profitWithItem = profit[currentItemIndex] + combinations(profit, weight, capacity - itemWeight, currentItemIndex + 1)

            # Do not add the item to the knapsack
            # Recursively call combinations
            #   increment the currentItemIndex
            profitWithoutItem = combinations(profit, weight, capacity, currentItemIndex + 1)

            return max(profitWithItem, profitWithoutItem)

    return combinations(profit, weight, capacity, 0)
