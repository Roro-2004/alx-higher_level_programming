#!/usr/bin/python3
def uppercase(strr):
    i = chr
    for i in strr:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
