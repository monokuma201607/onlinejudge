# coding: utf-8
while (1):
    m, f, r = map(int, raw_input().split())
    if (m == -1 and f == -1 and r == -1):
        break
    if(m == -1 or f == -1):
        print("F")
    else:
        if ((m + f) >= 80):
            print("A")
        elif (65 <= (m + f) < 80):
            print("B")
        elif (50 <= (m + f) < 65 or r >= 50):
            print("C")
        elif (30 <= (m + f) < 50 and (r == -1 or r < 50)):
            print("D")
        elif (30 > (m + f)):
            print("F")


