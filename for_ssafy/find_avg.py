def find_avg():
    T = int(input())
    for test_case in range(1, T + 1):
        ans = 0
        t = list(map(int,input().split()))
        ans = round(sum(t)/len(t))
        print(f'#{test_case} {ans}')

find_avg()