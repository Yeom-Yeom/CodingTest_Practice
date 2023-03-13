def check_mbti(survey,choices):
    answer = ''
    scores = [0]*8
    dic = {"R":0,"T":1,"C":2,"F":3,"J":4,"M":5,"A":6,"N":7}

    for i in range(len(survey)):
        score = choices[i]-4
        if score<0:
            scores[dic[survey[i][0]]] -= score
        elif score >0 :
            scores[dic[survey[i][1]]] += score

    answer+= 'T' if scores[0] < scores[1] else 'R'
    answer+= 'F' if scores[2] < scores[3] else 'C'
    answer+= 'M' if scores[4] < scores[5] else 'J'
    answer+= 'N' if scores[6] < scores[7] else 'A'

    return answer

# another solution
# def solution(survey, choices):
#   my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
#   for a,b in zip(survey,choices):
#       if a not in my_dict.keys():
#           a = a[::-1]
#           my_dict[a] -= b-4
#       else:
#           my_dict[a] += b-4
#
#   result = ""
#   for name in my_dict.keys():
#       if my_dict[name] > 0:
#           result += name[1]
#       elif my_dict[name] < 0:
#           result += name[0]
#       else:
#           result +=sorted(name)[0]
#
#   return result