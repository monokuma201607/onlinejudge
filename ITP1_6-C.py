# coding: utf-8
A_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0]]
A_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0]]
A_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0]]
A_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0,0]]
print len(A_1[0])
n = int(raw_input())
for i in range(0, n):
    b, f, r, v = map(int, raw_input().split())
    if '1' in str(b):
        A_1[f-1][r-1] += v
    if '2' in str(b):
        A_2[f - 1][r - 1] += v
    if '3' in str(b):
        A_3[f - 1][r - 1] += v
    if '4' in str(b):
        A_4[f - 1][r - 1] += v

acount = 0
for a1 in A_1:
    print"",
    print a1
    for a_1 in a1:
        print a_1,
        acount += 1
        if (acount % 9 == 0):
            print a_1
            acount += 1
print "#" * 20

bcount = 0
for a2 in A_2:
    print"",
    for a_2 in a2:
        print a_2,
        bcount += 1
        if (bcount % 10 == 0):
            print a_2
print "#" * 20

ccount = 0
for a3 in A_3:
    print"",
    for a_3 in a3:
        print a_3,
        ccount += 1
        if (ccount % 10 == 0):
            print a_3
print "#" * 20

dcount = 0
for a4 in A_4:
    print"",
    for a_4 in a4:
        print a_4,
        dcount += 1
        if (dcount % 10 == 0):
            print a_4
