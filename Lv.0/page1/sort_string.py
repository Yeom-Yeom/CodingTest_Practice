def sort_string(my_string):     
    return ''.join(sorted(my_string.lower()))
    # 우선 입력받은 my_string을 소문자로 치환 후 sorted() 함수로 정렬.
    # 정렬된 my_string은 배열 값이 되어 ''.join() 함수로 문자열로 변환.
print(sort_string("Bcad"))