def max_failures_in_window(failures, k):
    if k <= 0 or k > len(failures):
        return None

    window_sum = sum(failures[:k])
    max_failures = window_sum

    for j in range(k, len(failures)):
        window_sum = window_sum - failures[j - k] + failures[j]
        max_failures = max(max_failures, window_sum)

    return max_failures

failures = [2, 3, 4, 10, 12, 3, 2]
print(max_failures_in_window(failures, 3))
