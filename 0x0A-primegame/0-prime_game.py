#!/usr/bin/python3

"""Prime Game."""


def isWinner(x, nums):
    """Prime Game."""
    if x == 0 or not nums:
        return None

    # Sieve of Eratosthenes to find all primes up to 10000
    MAX_N = 10000
    is_prime = [True] * (MAX_N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(MAX_N ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, MAX_N + 1, i):
                is_prime[multiple] = False

    # Function to simulate one round
    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        num_moves = 0

        while primes:
            num_moves += 1
            first_prime = primes[0]
            # Remove the prime and its multiples
            primes = [p for p in primes if p % first_prime != 0]

        # Maria wins if num_moves is odd, Ben wins if even
        return 'Maria' if num_moves % 2 == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    # Play all rounds
    for n in nums:
        if n == 1:
            ben_wins += 1  # Ben wins if there are no primes (n == 1)
        else:
            winner = play_game(n)
            if winner == 'Maria':
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
