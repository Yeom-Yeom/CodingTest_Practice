def success_login(id_pw,db):
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

# 다른 사람의 풀이
# def solution(id_pw, db):
#   if db_pw := dict(db).get(id_pw[0])
#       return "login" if db_pw == id_pw[1] else "wrong pw"
#   return "fail"