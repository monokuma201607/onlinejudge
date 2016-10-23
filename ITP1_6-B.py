# coding: utf-8
S = ['S 1', 'S 2', 'S 3', 'S 4', 'S 5', 'S 6', 'S 7', 'S 8', 'S 9', 'S 10', 'S 11', 'S 12', 'S 13']
H = ['H 1', 'H 2', 'H 3', 'H 4', 'H 5', 'H 6', 'H 7', 'H 8', 'H 9', 'H 10', 'H 11', 'H 12', 'H 13']
C = ['C 1', 'C 2', 'C 3', 'C 4', 'C 5', 'C 6', 'C 7', 'C 8', 'C 9', 'C 10', 'C 11', 'C 12', 'C 13']
D = ['D 1', 'D 2', 'D 3', 'D 4', 'D 5', 'D 6', 'D 7', 'D 8', 'D 9', 'D 10', 'D 11', 'D 12', 'D 13']
cards = [S, H, C, D]
n = int(raw_input())
for i in range(0, n):
    a = raw_input()
    if 'S' in a:
        cards[0].remove(a)
    if 'H' in a:
        cards[1].remove(a)
    if 'C' in a:
        cards[2].remove(a)
    if 'D' in a:
        cards[3].remove(a)
for j in range(4):
    for i in cards[j]:
        print i
