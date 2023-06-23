def representation_of_numbers(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum+=j
            if sum == n:
                answer +=1
                break
            elif sum >n :
                break
    return answer

representation_of_numbers(15)

# another solution
# def solution(n):
#     return len([i for i in range(1,n+1, 2) if n % i is 0])