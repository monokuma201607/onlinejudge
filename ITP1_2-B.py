# coding: utf-8
import sys

# 整数の入力
a, b , c = map(int, raw_input().split())
if (0 <= a <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (0 <= b <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)

if (0 <= c <= 100):
    pass
else:
    print("Input Error ")
    sys.exit(1)

if(a < b < c ):
    print "Yes"
else:
    print "No"

sys.exit(0)
