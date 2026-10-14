def max_consecutive_failures(statuses):
    max_con_fail = 0
    con_fail = 0

    for status in statuses:
        if status == "FAIL":
            con_fail += 1
            max_con_fail = max(max_con_fail, con_fail)
        else:
            con_fail = 0

    return max_con_fail
