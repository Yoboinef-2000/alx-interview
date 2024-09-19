#!/usr/bin/python3

"""Change comes from within."""


def makeChange(coinValues, targetTotal):
    """Making Change."""
    if targetTotal <= 0:
        return 0

    fewestCoins = [float('inf')] * (targetTotal + 1)
    fewestCoins[0] = 0

    for coin in coinValues:
        for currentAmount in range(coin, targetTotal + 1):
            fewestCoins[currentAmount] = min(fewestCoins[currentAmount],
                                             fewestCoins[
                                                 currentAmount - coin] + 1)

    return fewestCoins[targetTotal] if fewestCoins[targetTotal] != \
        float('inf') else -1
