def cnt_duplication(array,n):
    answer =0 
    for arr in array:
        if n==arr:
            answer+=1
    return answer

# another solution
# def solution(array, n):
#   return array.count(n)