def arm_wrestling():
    T = int(input())
    for tc in range(1,T+1):
        wl = list(input().strip())
        ans = ''
        if len(wl) < 8:
            ans = 'YES'
        elif len(wl) == 8:
            if wl.count('o') >= 1:
                ans = 'YES'
            else : ans = 'NO'
        else:
            if wl.count('o')+(15-len(wl)) >= 8:
                ans = 'YES'
            else: ans = 'NO'
        print(f'#{tc} {ans}')

arm_wrestling()


