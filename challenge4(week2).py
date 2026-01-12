def count_payment_combinations(coins, total_sum):
    dp = [0] * (total_sum + 1)
    dp[0] = 1  # base case

    for coin in coins:
        for amount in range(coin, total_sum + 1):
            dp[amount] += dp[amount - coin]

    return dp[total_sum]
coins = [1, 2, 3]
total_sum = 4
print(count_payment_combinations(coins, total_sum))
coins2 = [2, 5, 3, 6]
total_sum2 = 10
print(count_payment_combinations(coins2, total_sum2))