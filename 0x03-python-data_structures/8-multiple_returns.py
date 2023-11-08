#!/usr/bin/python3
def multiple_returns(s):
    if len(s) == 0:
        return (0, 'None')
    else:
        return (len(s), s[0])
