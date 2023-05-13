def drawer_pw():
    T = list(map(int,input().split()))
    ans = 0
    for i in range(T[1], T[0]+1):
        ans+=1
    print(ans)
drawer_pw()