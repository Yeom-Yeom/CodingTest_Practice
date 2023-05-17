def valid_sudoku():
    def checkSudoku(M):
        for i in range(9):
            row_num = [0]*10
            col_num = [0]*10
            for j in range(9):
                row = M[i][j]
                col = M[j][i]
                if row_num[row] : return 0
                if col_num[col] : return 0

                row_num[row] = 1
                col_num[col] = 1

                if i%3 == 0 and j%3 == 0:
                    square = [0]*10
                    for r in range(i, i+3):
                        for c in range(j, j+3):
                            n = M[r][c]
                            if square[n]: return 0
                            square[n] = 1
        return 1
    T = int(input())
    for tc in range(1,T+1):
        mat = [list(map(int,input().split())) for _ in range(9)]
        ans = checkSudoku(mat)

        print(f'#{tc} {ans}')

