from base64 import b64decode
def base64_decoder():
    T = int(input())
    for tc in range(1,T+1):
        ans = ''
        Encoding = input()
        ans = b64decode(Encoding)
        ans= ans.decode('ascii')
        print(f'#{tc} {ans}')

base64_decoder()

T = int(input())
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]
for tc in range(1,T+1):
    word = list(input())

    length = len(word)

    res = ''
    for q in range(length):
        num = decode.index(word[q])
        bin_num = str(bin(num)[2:])
        while len(bin_num) < 6:
            bin_num = '0'+bin_num
        res += bin_num
    r = ''
    for w in range(length*6//8):
        e = int(res[w*8:w*8+8],2)

        r += chr(e)
    print(f'#{tc} {r}')