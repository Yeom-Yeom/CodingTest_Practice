def crane_drawing(board,moves):
    answer = []
    bucket=[]
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer+=bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer)*2

# another solution
# def solution(board, moves):
#   stacklist = []
#   answer = 0
#   for i in moves:
#       for j in range(len(board)):
#           if board[j][i-1] != 0:
#               stacklist.append(board[j][i-1])
#               board[j][i-1] = 0
#               if len(stacklist) >1 :
#                   if stacklist[-1] == stacklist[-2]:
#                       stacklist.pop(-1)
#                       stacklist.pop(-1)
#                       answer+=2
#               break
#   return answer