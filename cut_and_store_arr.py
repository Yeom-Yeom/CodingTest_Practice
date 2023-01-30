def cut_and_store_arr(my_str, n):
    answer = []
    if len(my_str)%n != 0: # 문자열 my_str을 n씩 자르고 남을 때
        for i in range(len(my_str)//n): # 우선 문자열 만큼 slice 후 answer 배열에 append
            answer.append(my_str[n*i:n*(i+1)])
        answer.append(my_str[n*(len(my_str)//n):]) # 남은 배열 slice[n:]로 끝까지 answer 배열에 append
    else:                  # 문자열 my_str을 n씩 자르고 남지 않을 때
        for i in range(len(my_str)//n): # n씩 자른 문자열을 answer 배열에 append
             answer.append(my_str[n*i:n*(i+1)])
    return answer # answer배열 반환

# def solution(my_str,n):
#   return [my_str[i: i+n] for i in range(0,len(my_str),n)]