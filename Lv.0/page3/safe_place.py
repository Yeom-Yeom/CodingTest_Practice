from collections import deque # deque : 스택과 큐의 기능을 한 번에 사용.
def safe_place(board):
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x,y):
        dq = deque()
        dq.append((x,y))
        while dq:
            a,b = dq.popleft() # pop left 왼쪽에서 값을 뺀다.
            visited[a][b] = True
            for i in range(8):
                nx = dx[i]+a
                ny = dy[i]+b
                if 0<=nx<length and 0<=ny<length and not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        dq.append((nx,ny))
                    else:
                        board[nx][ny] = 2
    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i,j)
    result = 0
    for i in range(length):
        result+= board[i].count(0)
    return result

# 다른 사람의 풀이
# def solution(board):
#   n = len(board)
#   danger = set()
#   for i, row in enumerate(board):
#       for j, x in enumerate(row):
#           if not x:
#               continue
#           danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1,0,1])
#   return n*n - sum(0<=i<n and 0<=j<n for i,j in danger)