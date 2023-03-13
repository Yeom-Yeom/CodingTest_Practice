def add_cnt_measure(left,right):
    result = 0
    for i in range(left,right+1):
        cnt=0
        for j in range(1, i+1):
            if i%j==0:
                cnt +=1
        if cnt%2==0:
            result+=i
        else:
            result-=i
    return result

# another solution
# def solution(left,right):
#   answer = 0
#   for i in range(left,right+1):
#       if int(i**0.5) == i**0.5:
#           answer -= i
#       else:
#           answer+=i
#   return answer