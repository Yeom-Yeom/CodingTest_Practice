def partner_num(X,Y):
    answer = ''
    for x in X:
        if x in Y:
            answer+=x
        if x in answer:
            answer-=x
    if len(answer)==0:
        return "-1"
    return sorted(answer,reverse=True)

print(partner_num("100","203045"))