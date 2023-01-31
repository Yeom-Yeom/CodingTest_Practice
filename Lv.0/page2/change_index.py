def change_index(my_string,num1,num2):
    answer=''
    my_string = list(my_string) # string을 list형식으로 변환
    my_string[num1],my_string[num2] = my_string[num2],my_string[num1] # list 형에서는 두 인덱스의 위치를 바꿀 수 있다. 
    return answer.join(my_string)