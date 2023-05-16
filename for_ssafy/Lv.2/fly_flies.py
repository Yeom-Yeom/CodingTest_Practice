def fly_flies():
    T = int(input())
    for tc in range(1,T+1):
        N,M = map(int,input().split())
        arr = [list(map(int,input().split())) for _ in range(N)]
        fly = []

        for i in range(N-M+1):
            for j in range(N-M+1):
                kill = 0
                for ki in range(M):
                    for kj in range(M):
                        if i+ki in range(N) and j+kj in range(N):
                            kill += arr[i+ki][j+kj]
                fly.append(kill)
        max_value = fly[0]
        for i in fly:
            if i > max_value:
                max_value = i
        print(f'#{tc} {max_value}')


