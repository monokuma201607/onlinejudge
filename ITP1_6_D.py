# coding: utf-8
n, m = map(int, raw_input().split())
a_list = []
for i in range(0, n):
    a_list.append(raw_input().split())

b_list = []
for i in range(0, m):
    b_list.append(raw_input())
c_list = []
for i in range(0, n):
    c_count = 0
    for j in range(0, m):
        a = int(a_list[i][j])
        b = int(b_list[j])
        c_count += a * b
    c_list.append(c_count)
    print c_list[i]
