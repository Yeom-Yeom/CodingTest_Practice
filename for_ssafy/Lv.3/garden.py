def garden():
    T = int(input())
    for tc in range(1,T+1):
        n,d = map(int,input().split())
        if (d*2)+1 == n:
            ans = 1
        else:
            if n%((d*2)+1) == 0:
                ans = n//((d*2)+1)
            else:
                ans = (n//((d*2)+1))+1
        print(f'#{tc} {ans}')

garden()

