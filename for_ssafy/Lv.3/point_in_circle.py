def point_in_circle():
    T = int(input())
    for tc in range(1,T+1):
        cnt = 0
        n = int(input())
        for i in range(-n-1,n+1):
            for j in range(-n-1,n+1):
                if i**2 + j**2 <= n**2:
                    cnt+=1
        print(f'#{tc} {cnt}')

point_in_circle()

