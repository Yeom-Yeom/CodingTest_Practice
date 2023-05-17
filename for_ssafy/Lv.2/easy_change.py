def easy_change():
    money = [50000,10000,5000,1000,500,100,50,10]
    T = int(input())
    for tc in range(1,T+1):
        cnt = [0]*8
        n = int(input())
        print(f'#{tc}')
        for i in range(len(money)):
            cnt[i] = int(n/money[i])
            n %= money[i]
            print(f'{cnt[i]}',end= " ")
        print("")


