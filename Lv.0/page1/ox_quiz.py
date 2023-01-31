def ox_quiz(quiz):
    answer = []
    for i in quiz:
        answer.append('O' if eval(i.replace('=','==')) else 'X')  # eval(expression) 함수 : 매개변수로 받은 expression(=식)을 문자열로 받아서, 실행하는 함수. '='는 대입연산자이므로 '=='로 대체.
    return answer