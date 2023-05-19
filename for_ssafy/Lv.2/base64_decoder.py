import base64
def base64_decoder():
    T = int(input())
    for tc in range(1,T+1):
        ans = ''
        Encoding = input()
        ans = base64.b64decode(Encoding)
        ans= ans.decode('ascii')
        print(f'#{tc} {ans}')
base64_decoder()