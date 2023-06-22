def infinite_str():
    T = int(input())
    for tc in range(1,T+1):
        s,t = map(str,input().split())
        if s*len(t) == t*len(s):
            print(f'#{tc} yes')
        else : print(f'#{tc} no')
        
infinite_str()



