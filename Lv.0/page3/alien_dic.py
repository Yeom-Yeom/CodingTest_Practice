def alien_dic(spell: list, dic: list):
    spell = {i : 0 for i in spell}

    for x in dic:
        if len(x) == len(spell):
            for y in x:
                if y in spell:
                    spell[y] +=1
                else:
                    break
            if len(set(spell.values())) ==1 and sum(set(spell.values())) ==1:
                return 1
            spell = {i: 0 for i in spell}
    return 2

# 다른 사람의 풀이
# def solution(spell,dic):
#   for d in dic:
#       if sorted(d) == sorted(spell):
#           return 1
#   return 2