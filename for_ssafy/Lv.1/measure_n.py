def measure_n():
    n = int(input())
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

measure_n()