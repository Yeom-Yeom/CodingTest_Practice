def cola_problem(a,b,n):
    answer = 0
    while n >=a:
        answer += (n//a)*b
        n = (n//a)*b+n%a

    return answer

# anther solution
# solution = lambda a,b,n : max(n-b,0)//(a-b)*b
