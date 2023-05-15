def rsp_1_by_1():
    rsp = list(map(int,input().split()))
    if rsp[0] > rsp[1]:
        print('A')
    else:
        print('B')
