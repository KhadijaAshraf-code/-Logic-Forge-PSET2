def min_cancelled_bookings(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    removals = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start < prev_end:
            # Overlap → remove this meeting
            removals += 1
        else:
            # No overlap → accept
            prev_end = end

    return removals
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(min_cancelled_bookings(intervals))
