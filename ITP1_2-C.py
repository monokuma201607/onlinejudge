# coding: utf-8
import sys

# 整数の入力
array = map(int, raw_input().split())
array.sort()
a = int(array[0])
b = int(array[1])
c = int(array[2])

if (1 <= a <= 10000):
    pass
else:
    print("Input Error ")
    sys.exit(1)
if (1 <= b <= 10000):
    pass
else:
    print("Input Error ")
    sys.exit(1)

if (1 <= c <= 10000):
    pass
else:
    print("Input Error ")
    sys.exit(1)

print str(a)+" "+str(b)+" "+str(c)

sys.exit(0)
