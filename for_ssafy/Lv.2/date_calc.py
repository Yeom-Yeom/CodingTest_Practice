def date_calc():
    T  = int(input())
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    for tc in range(1,T+1):
        date = list(map(int,input().split()))
        ans = 0
        if date[2] - date[0] == 0:
            print(f'#{tc} {date[3]-date[1]+1}')
            continue
        else:
            ans += (day[date[0]-1]-date[1])
            for i in range(date[0],date[2]-1):
                ans += day[i]
            ans += (date[3]+1)
        print(f'#{tc} {ans}')

date_calc()

