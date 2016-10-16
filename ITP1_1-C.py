# coding: utf-8
import sys

# 整数の入力
a, b = map(int, raw_input().split())
if (a < 1 or a > 100):
    print("Input Error ")
    sys.exit(1)
if (b < 1 or b > 100):
    print("Input Error ")
    sys.exit(1)

S = a * b
syuu = a * 2 + b * 2
print str(S) + " " + str(syuu)
sys.exit(0)
