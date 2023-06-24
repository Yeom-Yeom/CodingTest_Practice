def carpet(brown, yellow):
    size = brown + yellow
    for b in range(2, size+1):
        if size % b == 0 :
            a = size//b
            if a >= b:
                if 2*a + 2*b == brown+4:
                    return[a,b]

print(carpet(8,1))

# another solution
# def solution(brown, yellow):
#     for i in range(1, int(yellow**(1/2))+1):
#         if yellow % i == 0:
#             if 2*(i+yellow//i) == brown-4:
#                 return [yellow//i+2, i+2]