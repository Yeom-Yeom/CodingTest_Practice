def paint_grid():
    T = int(input())
    for tc in range(1,T+1):
        n,m = map(int,input().split())
        grid = [list(input().strip()) for _ in range(n)]
        check = [0]*4
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    if (i+j)%2 == 0:
                        check[0]+=1
                    else:
                        check[1]+=1
                elif grid[i][j] == '.':
                    if (i+j)%2 == 0:
                        check[2]+=1
                    else: check[3] +=1
        if (check[0] and check[1]) or (check[0] and check[2]) or (check[1] and check[3]) or (check[2] and check[3]):
            ans = 'impossible'
        else: ans = 'possible'
        print(f'#{tc} {ans}')

paint_grid()
