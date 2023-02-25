def cut_string(s):
    answer = 0
    t = ["",0,0] # 지정문자, 지정문자 수, 비교문자 수 

    for i in s:
        if t[0] == "":  # 처음 지정문자 잡아주기
            t[0] = i
            t[1] += 1
        else:
            if t[0] == i: # 지정문자 == 비교문자
                t[1]+=1
            else: # 지정문자 != 비교문자
                t[2]+=1
            if t[1] == t[2]: # 문자 수가 서로 같을 때
                answer+=1
                t = ["",0,0]
    if t != ["",0,0]:
        answer+=1
    return answer