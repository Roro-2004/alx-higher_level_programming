#!/usr/bin/python3
i = chr
for i in range(ord('a'), ord('z') + 1):
    if (i == 101) or (i == 113):
        continue
    else:
        print(chr(i).format(), end="")
