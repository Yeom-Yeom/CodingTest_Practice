def num_same_multiple():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        first = n
        ans = 'impossible'
        while first < (1e6):
            first += n
            tmp = list(map(int,str(first)))
            if sorted(list(map(int,str(n)))) == sorted(tmp):
                ans = 'possible'
                break
            else: continue
        print(f'#{tc} {ans}')

num_same_multiple()

