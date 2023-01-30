def push_string(A : str,B : str) -> int: # 변수는 str형 반환 값은 int형
    result = 0

    while result!= len(A): # result의 값이 A의 길이와 같을 때 까지
        if A==B: # A와 B가 동일하다면
            return result # 밀어낸 횟수 반환.
        A = A[-1] + A[:-1] # 슬라이스를 통해서 맨 마지막의 문자가 맨 앞으로 오도록 설정.
        result +=1 # 밀어낸 만큼 result 값 증가.
    return -1 # 문자열 A의 길이만큼 밀어내도 A와 B의 값이 같지 않다면 -1을 반환.

#solution = lambda a,b:(b*2).find(a) 