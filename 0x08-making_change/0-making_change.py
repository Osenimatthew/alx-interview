#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed to meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize DP array to store minimum coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin denomination
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If the total cannot be met by any combination of coins, return -1
    return dp[total] if dp[total] != float('inf') else -1
