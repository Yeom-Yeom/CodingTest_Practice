def competition_water_rate():
    T = int(input())
    for tc in range(1,T+1):
        n = list(map(int,input().split()))
        a_fee = n[4]*n[0]
        if n[2] > n[4]:
            b_fee = n[1]
        else:
            b_fee = n[1]+(n[4]-n[2])*n[3]
        if a_fee < b_fee :
            print(f'#{tc} {a_fee}')
        else:
            print(f'#{tc} {b_fee}')

competition_water_rate()