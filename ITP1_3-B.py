import sys

list=[]
for n in range(0,10001):
    x = int(raw_input())
    if (x == 0):
        break
    if (x < 1 or x > 10001):
        print("Input Error x")
        sys.exit(1)
    list.append(x)

for i, a in enumerate(list, 1):
    print "case "+str(i)+":"+" "+str(a)

sys.exit(0)
