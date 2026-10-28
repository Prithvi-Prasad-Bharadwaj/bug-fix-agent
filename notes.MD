## repo_01  

calculator.py :-

'''
sum(numbers) adds up the list.
len(numbers) counts the items.
The + 1 is the deliberate bug. A correct average divides by the count only, with no + 1.
'''

test_calculator.py

'''
Line 1 brings the average machine in from calculator.py.
The test asks: “Is the average of 2, 4, 6 equal to 4?”
'''

Bug: `+ 1` in the divisor. Fix: divide by len(numbers) only.


## repo_02 - utils.py

'''
This should add 1 + 2 + ... + n. range(1, n) stops before n, so n itself is never added. That’s the off-by-one bug.
'''

Bug: range(1, n) stops before n. Fix: range(1, n + 1).

## repo_03 - ride.py

'''
The rule says 18 and above can ride. age > 18 means “older than 18”, so a person who is exactly 18 is turned away. That’s the bug. The correct line is age >= 18.
'''

Bug: `>` instead of `>=`. Fix: age >= 18.
