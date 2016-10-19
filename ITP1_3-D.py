# coding: utf-8
import sys


def divisor(p):
    return [n for n in range(1, p+1) if p % n == 0]


# 整数の入力
a, b, c = map(int, raw_input().split())
if (a < 1 or a > 10000):
    print("Input Error a")
    sys.exit(1)
if (b < 1 or b > 10000):
    print("Input Error b")
    sys.exit(1)
if (c < 1 or c > 10000):
    print("Input Error c")
    sys.exit(1)
if (a > b):
    print("Input Error a b")
    sys.exit(1)

lists = divisor(c)
count = 0
for list in lists:
    if (a <= int(list) <= b):
        count += 1
print count
sys.exit(0)
