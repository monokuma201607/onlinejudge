# coding: utf-8
import sys

a_list=[]
for n in range(0,3001):
    list = map(int, raw_input().split())
    list.sort()
    x = int(list[0])
    y = int(list[1])
    if (x == 0 and y == 0):
        break
    if (x < 0 or x > 10001):
        print("Input Error x")
        sys.exit(1)
    if (y < 0 or y > 10001):
        print("Input Error x")
        sys.exit(1)
    a_list.append(list)
for i, a in enumerate(a_list, 1):
    x = int(a[0])
    y = int(a[1])
    print str(x) +" " + str(y)
sys.exit(0)