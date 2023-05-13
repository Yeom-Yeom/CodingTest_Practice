def add_digit():
    N = int(input())
    ans = 0
    while N != 0 :
        ans += (N%10)
        N = int(N/10)
    print(ans)

add_digit()