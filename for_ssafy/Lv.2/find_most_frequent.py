def find_most_frequent():
    T = int(input())
    for tc in range(1,T+1):
        n = int(input())
        arr = list(map(int,input().split()))
        freq= [0]*101
        mode = 0
        for a in arr:
                freq[a] += 1
                if freq[a] >= freq[mode]: mode = a
                print(f'#{tc} {mode}')
find_most_frequent()

