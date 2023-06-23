def convert_to_number(time):
    if ':' not in time:
        return int(time)
    a,b = time.split(':')

    return int(a)*60+int(b)

def working_on_assign(plans):
    p = []

    for title, start, time in plans:
        p.append((title, convert_to_number(start),convert_to_number(time)))
    p.sort(key = lambda x : x[1])
    ans = []
    stack = []
    for i in range(len(p)):
        if i == len(p)-1:
            ans.append(p[i][0])
            for i in range(-1, -len(stack)-1, -1):
                ans.append(stack[i][0])
            break
        extra = p[i+1][1] - (p[i][1]+p[i][2])

        if extra >= 0:
            ans.append(p[i][0])
            while stack:
                if stack[-1][1] <= extra :
                    k = stack.pop()
                    ans.append(k[0])
                    extra -= k[1]
                else:
                    stack[-1][1] -= extra
                    break
        else:
            stack.append([p[i][0],-extra])

    return ans

# another solution
# def solution(plans):
#     plans = sorted(map(lambda x: [x[0], int(x[1][:2])*60 + int(x[1][3:]),int(x[2])],plans), key = lambda x: -x[1])

#     lst = []
#     while plans:
#         x = plans.pop()
#         for i, v in enumerate(lst):
#             if v[0] > x[1]:
#                 lst[i][0] += x[2]
#         lst.append([x[1]+x[2], x[0]])
#     lst.sort()

#     return list(map(lambda x: x[1], lst))