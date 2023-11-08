#!/usr/bin/python3
def multiple_returns(s):
    if s is None:
        return (0, 'None')
    else:
        return (len(s), s[0])
