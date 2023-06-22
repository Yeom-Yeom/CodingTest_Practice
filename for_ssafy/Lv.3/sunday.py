def sunday():
    T = int(input())
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for tc in range(1,T+1):
        day = input()
        ans = 7-days.index(day)
        print(f'#{tc} {ans}')

sunday()

