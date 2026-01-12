from itertools import combinations

def maximize_freelance_profit(deadlines, profits):
    n = len(deadlines)
    max_profit = 0
    max_jobs = 0

    for r in range(1, n + 1):
        for subset in combinations(range(n), r):
            # sort selected jobs by deadline
            selected = sorted(subset, key=lambda i: deadlines[i])

            time = 0
            profit = 0
            valid = True

            for job in selected:
                time += 1
                if time > deadlines[job]:
                    valid = False
                    break
                profit += profits[job]

            if valid and profit > max_profit:
                max_profit = profit
                max_jobs = len(selected)

    return [max_jobs, max_profit]
print(maximize_freelance_profit([4,1,1,1], [20,10,40,30]))
# Output: [2, 60]

