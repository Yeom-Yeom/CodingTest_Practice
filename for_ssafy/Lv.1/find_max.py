def find_max():
    T = int(input())
    for test_case in range(1, T+1):
        t = list(map(int,input().split()))
        ans = max(t)
        print(f'#{test_case} {ans}')

find_max()