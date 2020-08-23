def solution(profit: [int], weight: [int], capacity: int) -> int:
    m = len(profit) + 1
    n = capacity+1

    # Create a 2 dimensional matrix
    # Row = item
    # Col = capacity
    dp = [[0]*n for _ in range(m)]

    # Iterate over the matrix
    for i in range(1, m):
        for j in range(1, n):
            itemWeight = weight[i-1]

            # if the item can fit into the backpack
            #   use the max profit of including the item vs not including the item
            # otherwise
            #   use the max profit when not including the item
            if itemWeight <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-itemWeight] + profit[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
