def bigger_same_smaller():
    T = int(input())
    for test_case in range(1,T+1):
        t = list(map(int,input().split()))
        if t[0] < t[1]:
            print(f'#{test_case} <')
        elif t[0] == t[1]:
            print(f'#{test_case} =')
        else:
            print(f'#{test_case} >')

bigger_same_smaller()