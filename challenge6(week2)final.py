def maximize_freelance_profit(deadlines, profits):
    jobs = list(zip(deadlines, profits))
    jobs.sort(key=lambda x: x[1], reverse=True)  # sort by profit

    max_deadline = max(deadlines)
    slots = [-1] * (max_deadline + 1)

    job_count = 0
    total_profit = 0

    for deadline, profit in jobs:
        for t in range(deadline, 0, -1):
            if slots[t] == -1:
                slots[t] = profit
                job_count += 1
                total_profit += profit
                break

    return [job_count, total_profit]

print(maximize_freelance_profit([4,1,1,1], [20,10,40,30]))
# Output: [2, 60]



