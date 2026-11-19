#!/usr/bin/python3
"""Find the minimum number of coins needed to make change."""


def makeChange(coins, total):
    """Return the fewest coins needed, or -1 if total is unreachable."""
    if total <= 0:
        return 0

    values = sorted(set(coin for coin in coins if coin <= total))
    if not values:
        return -1

    largest = values[-1]
    if total % largest == 0:
        return total // largest

    unreachable = total + 1
    fewest = [unreachable] * (total + 1)
    fewest[0] = 0

    for coin in values:
        for amount in range(coin, total + 1):
            candidate = fewest[amount - coin] + 1
            if candidate < fewest[amount]:
                fewest[amount] = candidate

    return -1 if fewest[total] == unreachable else fewest[total]
