# coding: utf-8
import sys

# 整数の入力
a, b = map(int, raw_input().split())
if (-1000 <= a <= 1000):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (-1000 <= b <= 1000):
    pass
else:
    print("Input Error ")
    sys.exit(1)

if a > b:
    print "a > b"
elif a < b :
    print "a < b"
else:
    print "a == b"

sys.exit(0)
