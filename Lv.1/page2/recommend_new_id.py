import re
def recommend_new_id(new_id):
    new_id = new_id.lower()
    answer = re.sub(r"[^a-zA-Z0-9-_.]","",new_id)
    while '..' in answer:
        answer = answer.replace('..','.')
    
    if answer[0] == '.':
        answer = answer[1:] if len(answer) >1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer='a'
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) < 3:
        answer+=answer[-1]

    return answer
    
# another solution
# def solution(new_id):
#   st = new_id
#   st = st.lower()
#   st = re.sub('[^a-z0-9\-_.]','',st)
#   st = re.sub('\.+','',st)
#   st = re.sub('^[.]|[.]$','',st)
#   st = 'a' if len(st) == 0 else st[:15]
#   st = re.sub['^[.]|[.]$','',st)
#   st = st if len(st)>2 else st + "".join([st[-1] for i in range(3-len(st))])
#   return st