def scored_by_TA():
    T = int(input())
    grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for tc in range(1,T+1):
        N,K = map(int,input().split())
        ans = []
        _max = n//10
        for idx, value in enumerate(range(n)):
            m, f, a = map(int,input().split())
            ans.append((idx+1, (m*.035+f*0.45+a*0.2)))
            ans.sort(reverse=True, key = lambda x : x[1])
        tmp = [x[0] for x in ans]
        print(f'#{tc} {grades[(tmp.index(k))//_max]}')
