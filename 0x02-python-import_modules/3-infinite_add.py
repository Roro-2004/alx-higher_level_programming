#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = len(sys.argv) - 1
    x = 0
    for i in range(r):
        x += int(sys.argv[i + 1])

    print(x)
