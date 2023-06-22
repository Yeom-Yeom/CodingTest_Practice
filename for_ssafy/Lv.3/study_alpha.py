def study_alpha():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    T = int(input())
    for tc in range(1,T+1):
        arr = input()
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == alpha[i]:
                cnt +=1
            else:
                break
        print(f'#{tc} {cnt}')

study_alpha()

