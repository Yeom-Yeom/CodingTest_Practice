import math
def walking_multi_table():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        cnt = n+2
        for i in range(1,int(math.sqrt(n))+1):
            if n%i == 0 and cnt > (n//i)+i:
                cnt = (n//i)+i
                print(cnt)
        print(f'#{tc} {cnt-2}')

walking_multi_table()
