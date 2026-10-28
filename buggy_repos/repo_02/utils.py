def sum_up_to(n):
    total = 0
    for i in range(1, n):
        total += i
    return total

'''
This should add 1 + 2 + ... + n. range(1, n) stops before n, so n itself is never added. That’s the off-by-one bug.
'''