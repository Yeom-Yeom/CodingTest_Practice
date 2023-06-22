def go_rc():
    T = int(input())
    for tc in range(1,T+1):
        N = int(input())
        distance = 0
        s = 0 #speed
        for _ in range(N):
            value = input().split()
            if value[0] == '1':
                s += int(value[1])
                distance += s
            elif value[0] == '2':
                if s < int(value[1]) :
                    s = 0
                    distance = distance
                else:
                    s -= int(value[1])
                    distance += s
            else:
                s = s
                distance += s
        print(f'#{tc} {distance}')

go_rc()

