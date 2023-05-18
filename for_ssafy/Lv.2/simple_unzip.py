def simple_unzip():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        print(f'#{tc}')
        ans = ""
        cnt = 0
        for _ in range(n):
            ci = list(map(str,input().split()))
            ans+= (ci[0]*int(ci[1]))
            cnt += int(ci[1])
        for i in range(round(cnt/10)+1):
            print(ans[i*10:i*10+10])

simple_unzip()


