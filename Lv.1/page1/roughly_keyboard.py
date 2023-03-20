def roughly_keyboard(keymap, targets):
    keytable={}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i+1
            else:
                keytable[key] = min(keytable[key],i+1)
    answer = []
    for target in targets:
        clicked=0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked+=keytable[key]
        answer.append(clicked)

    return answer

# another solution
# def solution(keymap, targets):
#   kdist = dict()
#   for s in keymap:
#       for i in range(len(s)):
#           kdist.setdefulat(s[i],100)
#           kdist[s[i]] = min(kdist[s[i]],i+1)
#   answer = []
#   for s in targets;
#       cnt = 0
#       flag = 0
#       for i in range(len(s)):
#           if s[i] not in kdist:
#               flag = 1
#               break
#           cnt+=kdist[s[i]]
#       if flag == 1 : answer.append(-1)
#       else : answer.append(cnt)
#   return answer