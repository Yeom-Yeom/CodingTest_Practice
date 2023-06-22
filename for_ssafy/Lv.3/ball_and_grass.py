def ball_and_grass():
    T = int(input())
    for tc in range(1,T+1):
        cnt = 0
        gl = input() # gl = grassland
        for i in range(len(gl)-1):
            if (gl[i] == '(' and gl[i+1] == ')') or (gl[i] == '|' and gl[i+1] == ')') or (gl[i] == '(' and gl[i+1] == '|'):
                cnt+=1
        print(f'#{tc} {cnt}')

ball_and_grass()

