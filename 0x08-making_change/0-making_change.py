#!/usr/bin/python3

from collections import deque
"""Change comes from within."""


def makeChange(coins, total):
    """THe change maker."""
    if total == 0:
        return 0
    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_sum, num_coins = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum == total:
                return num_coins + 1

            if next_sum < total and next_sum not in visited:
                visited.add(next_sum)
                queue.append((next_sum, num_coins + 1))

    return -1
