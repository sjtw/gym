from typing import List

def max_profit(prices: List[int]) -> int:
    s = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            s += prices[i + 1] - prices[i]
    return s