def find_number(num, k):
    for i in str(num): # num을 문자열로 변환 후 하나씩 비교
        if i == str(k): # 비교한 문자가 k와 같다면,
            return str(num).index(str(k))+1 # k의 index값(=위치)+1, index는 0부터 시작이므로 +1
    return -1

# 다른 사람의 풀이
# def solution(num,k):
#   return -1 if str(k) not in str(num) else str(num.find(str(k))+1