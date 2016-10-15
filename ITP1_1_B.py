# coding: utf-8
import sys
# 整数の入力
x = int(raw_input())
if (x < 1 or x > 100):
    print("Input Error ")
    sys.exit(1)

print x * x * x
