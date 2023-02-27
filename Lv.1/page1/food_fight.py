def food_fight(food):
    res_1=''
    res_2=''
    tmp=[]
    for f in food:
        tmp.append(f//2)
    for i in range(len(tmp)):
        if tmp[i] == 0:
            continue
        else:
            for j in range(tmp[i]):
                res_1+=str(i)
                res_2+=str(i)
    res_2 = res_2[::-1]
    answer=res_1+"0"+res_2
    return answer

# another solution
# def solution(food):
#   answer = ''
#   for i,n in enumerate(food[1:]):
#       answer += str(i+1)*(n//2)
#   return answer+"0"+answer[::-1]