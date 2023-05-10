def add_odd():
    T = int(input())

    for test_case in range(1, T + 1):
        ans = 0
        for t in list(map(int,input().split())):
            if t %2 == 1:
                ans += t
        print(f'{test_case} {ans}')
add_odd()

