#!/usr/bin/python3
"""

"""


def OptimusPrimo(n):
    """

    """
    Sentinel = []
    HotRod = [True] * (n + 1)
    for cybertron in range(2, n + 1):
        if (HotRod[cybertron]):
            Sentinel.append(cybertron)
            for i in range(cybertron, n + 1, cybertron):
                HotRod[i] = False
    return Sentinel


def isWinner(x, nums):
    """
    
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        Sentinel = OptimusPrimo(nums[i])
        if len(Sentinel) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
