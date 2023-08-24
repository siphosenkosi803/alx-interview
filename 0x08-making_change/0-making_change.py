#!/usr/bin/python3
""" 0x08. Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total"""

    if total <= 0:
        return 0
    else:
        from math import trunc

        coins = sorted(coins, reverse=True)
        penny_royale = {}
        while total is not None:
            for i in coins:
                if total % i == 0:
                    penny_royale[i] = total / i
                    return(int(sum(penny_royale.values())))
                else:
                    penny_royale[i] = trunc(total / float(i))
                    total -= (i * penny_royale[i])
            return -1

