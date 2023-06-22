def rook_on_chess():
    T = int(input())
    def cnt():
        row = [0,0,0,0,0,0,0,0]
        col = [0,0,0,0,0,0,0,0]
        count = 0
        for i in range(8):
            for j in range(8):
                if rook[i][j] == 'O':
                    row[i] += 1
                    col[j] +=1
                    count+=1
                    if row[i]>=2 or col[j] >= 2:
                        return False
        if count == 8:
            return True
        else : return False
    for tc in range(1,T+1):
        rook = [list(input().strip()) for _ in range(8)]
        if cnt():
            print(f'#{tc} yes')
        else: print(f'#{tc} no')
rook_on_chess()

