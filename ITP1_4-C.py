# coding: utf-8
import sys
while 1:
    list = raw_input().split()
    a = int(list[0])
    op = list[1]
    b = int(list[2])

    if(op == "+"):
        print(a + b)
    elif(op == "*"):
        print(a * b)
    elif(op == "/"):
        print(a / b)
    elif(op == "-"):
        print(a - b)
    elif(op == "?"):
        break

