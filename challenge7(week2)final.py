import math

def calculate_minimum_speed(piles, k):
    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= k:
            answer = mid
            right = mid - 1  # try slower speed
        else:
            left = mid + 1   # need faster speed

    return answer

print(calculate_minimum_speed([5,10,3], 4))
# Output: 5


