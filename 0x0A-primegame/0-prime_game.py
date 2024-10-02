#!/usr/bin/python3
"""
Prime Game - A game where players take turns picking prime numbers and
removing them and their multiples. Maria plays first, and both play optimally.
"""


def sieve_of_eratosthenes(max_n):
    """Generates a list of prime numbers up to max_n."""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, max_n + 1, start):
                sieve[i] = False
    return sieve


def count_primes_up_to_n(n, primes):
    """Counts how many primes exist up to the given number n."""
    return sum(primes[2:n + 1])


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the Prime Game.

    Args:
    x: Number of rounds.
    nums: List of integers, where each integer represents n in that round.

    Returns:
    The name of the player who won the most rounds or None if it's a draw.
    """
    if not nums or x <= 0:
        return None

    # Find the maximum n in nums to limit prime sieve computation
    max_n = max(nums)

    # Generate primes up to the maximum number in nums
    primes = sieve_of_eratosthenes(max_n)

    # Variables to count the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each game
    for n in nums:
        prime_count = count_primes_up_to_n(n, primes)

        # If the count of prime moves is odd, Maria wins, else Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
