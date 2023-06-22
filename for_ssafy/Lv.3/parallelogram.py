def parallelogram():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        ans = 0
        width = n
        height = n
        ans = width*height
        print(f'#{tc} {ans}')

parallelogram()

