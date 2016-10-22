# coding: utf-8
N = int(raw_input())
print "",
for n in range(3, N + 1):
    if (n % 3 == 0 or '3' in str(n)):
        print str(n),
