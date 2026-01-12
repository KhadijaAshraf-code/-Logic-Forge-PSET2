import math

def calculate_minimum_speed_bruteforce(piles, k):
    max_pile = max(piles)

    for speed in range(1, max_pile + 1):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)

        if hours <= k:
            return speed

print(calculate_minimum_speed([5,10,3], 4))
# Output: 5
