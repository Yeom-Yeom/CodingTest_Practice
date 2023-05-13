import math
def double_double():
    n = int(input())
    for i in range(0,n+1):
        print(int(math.pow(2,i)),end=" ")

double_double()