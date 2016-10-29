# coding:utf-8
import itertools

while (1):
    n, x = map(int, raw_input().split())
    if (n == 0 and x == 0):
        break
    list_A = []
    for i in range(1, n + 1):
        list_A.append(i)
    combs = list(itertools.combinations(list_A, 3));
    count = 0
    for comb in combs:
        a = comb[0]
        b = comb[1]
        c = comb[2]
        sum_con = a + b + c
        if (sum_con == x):
            count += 1
    print count
