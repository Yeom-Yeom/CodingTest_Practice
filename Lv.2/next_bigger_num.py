def next_bigger_num(n):
    answer = n+1
    while True:
        a = bin(n)
        b = bin(answer)
        if a.count('1') == b.count('1'):
            return answer
        else:
            answer+=1
        
print(next_bigger_num(78))