import sys
write = sys.stdout.write
while 1:
    H, W = map(int, raw_input().split())
    if (H == 0 and W == 0):
        break
    else:
        for j in range(H):
            for k in range(W):
                if (j + k) % 2 == 0:
                    write("#")
                else:
                    write(".")
            print ""
        print ""
