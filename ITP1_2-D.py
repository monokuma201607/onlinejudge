# coding: utf-8
import sys
# 整数の入力
W, H, x, y, r = map(int, raw_input().split())
if (-100 <= x <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (-100 <= y <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)

if (0 <= W <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (0 <= H <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (0 <= r <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)

x_min = x - r
x_max = x + r
y_min = y - r
y_max = y + r

if(0 <= x_min <= W and 0 <= x_max <= W and 0 <= y_min <= H and 0 <= y_max <= H ):
    print"Yes"
else:
    print"No"
sys.exit(0)