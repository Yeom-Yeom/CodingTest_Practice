def similarity_arr(s1,s2): # 가장 쉬운 brute-force 방법으로 일일이 비교. 문제점은 시간 복잡도 증가.
    answer = 0
    for i in s1:
        for j in s2:
            if j == i:
                answer+=1
    return answer

# 다른 사람의 문제 풀이
# def solution(s1,s2):
#   return len(set(s1)&set(s2))