while 1:
    H, W = map(int, raw_input().split())
    if (H == 0 and W == 0):
        break
    else:
        for h in range(H):
            if (h == 0 or h == H - 1):
                print'#' * W
            else:
                print'#' + "." * (W - 2) + '#'
        print ''
