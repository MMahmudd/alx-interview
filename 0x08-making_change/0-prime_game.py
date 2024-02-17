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
    # sort the coins in descending order
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
