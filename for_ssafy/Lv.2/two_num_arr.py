def two_num_arr():
    T = int(input())
    for tc in range(1,T+1):
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        ans=[]
        if len(a)<len(b):
            for i in range(len(b)-len(a)+1):
                tmp = 0
                for j in range(len(a)):
                    tmp += (a[j]*b[i+j])
                ans.append(tmp)
        else :
            for i in range(len(a)-len(b)+1):
                tmp = 0
                for j in range(len(b)):
                    tmp += (a[i+j]*b[j])
                ans.append(tmp)
        print(ans)
        print(f'#{tc} {max(ans)}')
two_num_arr()

# T = int(input())
# for tc in range(1,T+1):
#     n,m = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     ans=[]
#     if len(a)<len(b):
#         for i in range(len(b)-len(a)):
#             tmp = 0
#             for j in range(len(a)):
#                 tmp += (a[j]*b[i+j])
#             ans.append(tmp)
#     else :
#         for i in range(len(a)-len(b)):
#             tmp = 0
#             for j in range(len(b)):
#                 tmp += (a[i+j]*b[j])
#             ans.append(tmp)