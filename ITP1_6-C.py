# coding: utf-8
A_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
A_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
A_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
A_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = int(raw_input())
for i in range(0, n):
    b, f, r, v = map(int, raw_input().split())
    if '1' in str(b):
        A_1[f - 1][r - 1] += v
    if '2' in str(b):
        A_2[f - 1][r - 1] += v
    if '3' in str(b):
        A_3[f - 1][r - 1] += v
    if '4' in str(b):
        A_4[f - 1][r - 1] += v

acount = 0
for a1 in A_1:
    print"",
    for (i, a_1) in enumerate(a1):
        if (i == 9):
            print a_1
            break
        print a_1,
print "#" * 20

bcount = 0
for a2 in A_2:
    print"",
    for (i, a_2) in enumerate(a2):
        if (i == 9):
            print a_2
            break
        print a_2,
print "#" * 20

ccount = 0
for a3 in A_3:
    print"",
    for (i, a_3) in enumerate(a3):
        if (i == 9):
            print a_3
            break
        print a_3,
print "#" * 20

dcount = 0
for a4 in A_4:
    print"",
    for (i, a_4) in enumerate(a4):
        if (i == 9):
            print a_4
            break
        print a_4,
