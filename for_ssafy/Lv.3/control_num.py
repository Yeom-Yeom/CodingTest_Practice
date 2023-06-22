from itertools import combinations
def control_num():
    T = int(input())
    for tc in range(1,T+1):
        n = list(x for x in input())
        target = [i for i in range(len(n))]
        min_n, max_n = int(''.join(n)), int(''.join(n))

        for value in combinations(target,2):
            i,j = value
            n[i],n[j] = n[j],n[i]
            if n[0] == '0':
                n[i],n[j] = n[j],n[i]
                continue
            if int(''.join(n)) < min_n:
                min_n = int(''.join(n))
            if int(''.join(n)) > max_n:
                max_n = int(''.join(n))
            n[i],n[j] = n[j],n[i]
        print(f'#{tc} {min_n} {max_n}')

control_num()