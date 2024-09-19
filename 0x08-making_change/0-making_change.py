#!/usr/bin/python3
"""
Module for the makeChange function.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): List of the values of the coins.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed,
        or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        count = total // coin
        coin_count += count
        total -= coin * count

    if total != 0:
        return -1
    return coin_count
