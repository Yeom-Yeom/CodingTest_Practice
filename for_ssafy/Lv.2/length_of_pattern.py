def length_of_pattern():
    T = int(input())
    for tc in range(1,T+1):
        pattern = str(input())
        for i in range(1,30):
            if pattern[:i] == pattern[i:i+i]:
                print(f'#{tc} {i}')
                break
length_of_pattern()

