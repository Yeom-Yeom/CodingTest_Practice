def share_remainder():
    T = int(input())
    for test_case in range(1, T+1):
        t = list(map(int,input().split()))
        print(f'#{test_case} {int(t[0]/t[1])} {t[0]%t[1]}')


