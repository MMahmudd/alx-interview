#!/usr/bin/python3
"""docum"""

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win_round(primes, n):
        if n % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    if x <= 0 or not nums:
        return None

    total_wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes(n)
        round_winner = can_win_round(primes, n)
        total_wins[round_winner] += 1

    if total_wins["Maria"] > total_wins["Ben"]:
        return "Maria"
    elif total_wins["Maria"] < total_wins["Ben"]:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
