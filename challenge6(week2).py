def maximize_freelance_profit(deadlines, profits):
    n = len(deadlines)
    max_deadline = max(deadlines)
    used = [False] * max_deadline

    max_profit = 0
    max_jobs = 0

    def backtrack(job_index, jobs_done, profit):
        nonlocal max_profit, max_jobs

        # Update best result
        if profit > max_profit:
            max_profit = profit
            max_jobs = jobs_done

        if job_index == n:
            return

        # Option 1: Skip this job
        backtrack(job_index + 1, jobs_done, profit)

        # Option 2: Try to schedule this job
        for t in range(deadlines[job_index]):
            if not used[t]:
                used[t] = True
                backtrack(job_index + 1, jobs_done + 1, profit + profits[job_index])
                used[t] = False

    backtrack(0, 0, 0)
    return [max_jobs, max_profit]
print(maximize_freelance_profit([4,1,1,1], [20,10,40,30]))
# Output: [2, 60]



