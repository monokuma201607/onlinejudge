# coding: utf-8
import sys

S = int(raw_input())
if (0 <= S < 86400):
    pass
else:
    print("Input Error ")
    sys.exit(1)

M = S / 60
s = S % 60
m = M % 60
H = M / 60
h = H % 60

print str(h) + ":" + str(m) + ":" + str(s)
sys.exit(0)
