from itertools import permutations # 순열(permutations)을 사용하기 위한 선언, 조합(combination)을 사용할 때도 itertools 선언.
def babbling(b): 
    answer = 0
    lst = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(lst)+1):
        for j in permutations(lst,i): # 예를 들어 (a,b,c)라는 lst가 있다면, (a,b),(a,c),(b,a),(b,c),(c,a),(c,b) 라는 순열로 표현가능.
            word.append(''.join(j)) # word배열에 join으로 순열로 만든 리스트 하나씩 join

    for i in b: # 매개변수로 받은 리스트 요소 하나씩
        if i in word: # 그 요소들 중에 word배열에 들어있다면 네 가지 발음 중 조합이 가능한 단어.
            answer+=1 
    return answer

# 다른 사람의 풀이
# def solution(babbling):
#     c = 0
#     for b in babbling :
#         for w in ["aya","ye","woo","ma"]:
#             if w*2 not in b :
#                 b = b.replace(w, ' ')
#             if len(b.strip()) == 0:
#                 c+=1
#         return c