def triangle_pascal():
    T = int(input())

    for tc in range(1, T+1):
        ans = []
        N = int(input())
        for i in range(N):
            tmp = []
            for j in range(i+1):
                if j==0 or j==i:
                    tmp.append(1)
                else:
                    tmp.append(ans[i-1][j]+ans[i-1][j-1])
            ans.append(tmp)
        print(f'#{tc} ')
        for i in ans:
            print(*i)