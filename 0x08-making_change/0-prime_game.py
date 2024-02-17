#!/usr/bin/python3
"""
Interview_Question_on:_fewest_number_of_coins_needed_to
meet_a_given_amount_total
"""

from __future__ import print_function
import sys

def makeChange(coins, total):
    """ fewest_number_of_coins_needed_t_meet_total """
    if total <= 0:
        return 0
    # sort_the_coins _n_ descending_order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change

def main():
    coins = [25, 10, 5, 1]
    total = 63

    result = makeChange(coins, total)
    if result != -1:
        print("{} coins needed to make a total of {}".format(result, total))
    else:
        print("It's not possible to make the total with the given coins.")

if __name__ == "__main__":
    main()
