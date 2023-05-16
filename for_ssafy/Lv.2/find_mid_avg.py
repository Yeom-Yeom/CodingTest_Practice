def find_mid_avg():
    T = int(input())
    for tc in range(1,T+1):
        n = list(map(int,input().split()))
        ans = 0
        n = sorted(n)[1:-1]
        ans = round(sum(n)/len(n))
        print(f'#{tc} {ans}')

