def where_can_word_in():
    T = int(input())
    for tc in range(1,T+1):
        n,k = map(int,input().split())
        cnt = 0
        arr = [list(map(int,input().split())) for _ in range(n)]
        for i in range(n):
            tmp = 0
            for j in range(n):
                if arr[i][j] == 0:
                    if tmp == k:
                        cnt+=1
                    tmp =0
                    continue
                tmp+=1
            if tmp == k:
                cnt+=1

        for i in range(n):
            tmp = 0
            for j in range(n):
                if arr[j][i] == 0:
                    if tmp == k:
                        cnt+=1
                    tmp =0
                    continue
                tmp+=1
            if tmp == k:
                cnt+=1


        print(f'#{tc} {cnt}')

