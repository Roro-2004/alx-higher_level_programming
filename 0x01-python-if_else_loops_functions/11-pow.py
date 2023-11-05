#!/usr/bin/python3
def pow(a, b):
    ans = 1
    x = 0
    if b < 0:
        b = b * -1
        x = 1
    for i in range(b):
        ans = ans * a
    if x == 1:
        b = b * -1
    if b > 0:
        return ans
    elif b < 0:
        return float(1 / ans)
    else:
        return 1
