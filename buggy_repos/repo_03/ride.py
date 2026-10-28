def can_ride(age):
    return age > 18

'''
The rule says 18 and above can ride. age > 18 means “older than 18”, so a person who is exactly 18 is turned away. That’s the bug. The correct line is age >= 18.
'''