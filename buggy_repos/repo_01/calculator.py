def average(numbers):
    return sum(numbers) / (len(numbers) + 1)

'''
sum(numbers) adds up the list.
len(numbers) counts the items.
The + 1 is the deliberate bug. A correct average divides by the count only, with no + 1.
'''