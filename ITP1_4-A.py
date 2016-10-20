# coding: utf-8
import sys

a, b = map(int, raw_input().split())
d = a // b
r = a % b
f = float(a) / b

print('%s %s %.5f' % (d, r, f))

sys.exit(0)
