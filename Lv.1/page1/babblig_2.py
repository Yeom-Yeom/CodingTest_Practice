def babbling_2(babbling):
    answer=0
    for b in babbling:
        for i in ['aya','ye','woo','ma']:
            if i*2 not in b:
                b=b.replace(i,' ')
        if len(b.strip()) == 0:
            answer+=1
    return answer