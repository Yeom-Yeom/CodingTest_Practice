def mock_exam(answers):
    a = [1,2,3,4,5]*len(answers)
    b = [2,1,2,3,2,4,2,5]*len(answers)
    c = [3,3,1,1,2,2,4,4,5,5]*len(answers)
    tmp=[0,0,0]
    answer=[]
    for x,n in zip(a,answers):
        if x == n:
            tmp[0]+=1
    for x,n in zip(b,answers):
        if x == n:
            tmp[1] +=1
    for x,n in zip(c, answers):
        if x == n:
            tmp[2]+=1
    print(tmp)
    if tmp[0] == max(tmp):
        answer.append(1)
    if tmp[1] == max(tmp):
        answer.append(2)
    if tmp[2] == max(tmp):
        answer.append(3)
    return answer

# another solution
# def solution(answers):
#   a = [1,2,3,4,5]
#   b = [2,1,2,3,2,4,2,5]
#   c = [3,3,1,1,2,2,4,4,5,5]
#   score = [0,0,0]
#   result = []
#   for idx, answer in enumerate(answers):
#       if answer == a[idx%len(a)]:
#           score[0]+=1
#       if answer == b[idx%len(b)]:
#           score[1]+=1
#       if answer == c[idx%len(c)]:
#           score[2]+=1
#   for idx, s in enumerate(score):
#       if s == max(score):
#           result.append(idx+1)
#   return result