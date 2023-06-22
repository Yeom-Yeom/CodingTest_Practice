def simple_factorization():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        ans = [0]*5
        while n%2 == 0:
            n/=2
            ans[0]+=1
        while n%3 == 0:
            n/=3
            ans[1] +=1
        while n%5 == 0:
            n/=5
            ans[2] +=1
        while n%7 ==0:
            n/= 7
            ans[3] +=1
        while n%11 == 0:
            n/=11
            ans[4] +=1
        print(f'#{tc}',end=" ")
        for i in ans:
            print(i,end=' ')
        print()

simple_factorization()

