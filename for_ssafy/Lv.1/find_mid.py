def find_mid():
    T = int(input())
    t = list(map(int,input().split()))
    t.sort()
    print(t[int(T/2)])

find_mid()