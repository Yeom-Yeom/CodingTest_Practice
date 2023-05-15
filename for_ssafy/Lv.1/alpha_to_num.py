def alpha_to_num():
    alpha = str(input())
    for a in alpha:
        ans = ord(a) - 64
        print(ans,end=" ")
