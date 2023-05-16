def check_circular():
    T = int(input())
    for tc in range(1,T+1):
        words = str(input())
        tmp = ""
        for w in reversed(words):
            tmp+=w
        if words == tmp:
            print(f"#{tc} 1")
        else:
            print(f"#{tc} 0")

check_circular()


