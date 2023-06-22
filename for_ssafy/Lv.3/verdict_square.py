def verdict_square():
	
    t = int(input())
    for test_case in range(1,t+1):
        n = int(input())
        board = []
        for _ in range(n):
            board.append(list(input()))
        point = 0
        for i in range(n):
            point += board[i].count("#")
        length = point ** 0.5
        ans = 0
        cnt = 0
        for i in range(n):
            for j in range(n):
    
                if board[i][j] == "#":
                    for y in range(i, i+int(length)):
                        for x in range(j, j+int(length)):
                            if board[y][x] == "#":
                                cnt += 1
                    break
            if cnt!=0:
                break
    
        if cnt == point:
            print("#{} {}".format(test_case, "yes"))
        else:
            print("#{} {}".format(test_case, "no"))

verdict_square()

